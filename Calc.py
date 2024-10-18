from itertools import product

def evaluate_expression(numbers, operators):
    """Evaluate an expression built from numbers and operators."""
    if not numbers:
        return None
    expression = str(numbers[0])
    for op, num in zip(operators, numbers[1:]):
        expression += f' {op} {num}'
    try:
        return eval(expression)
    except ZeroDivisionError:
        return None

def find_min_operators(allowed_numbers, target):
    """Find the minimum number of operators to reach the target number."""
    min_operators = float('inf')
    solutions = []
    operators = ['+', '-', '*', '/']

    # Step 1: Brute force to find the minimum number of operators
    for op_count in range(len(allowed_numbers) - 1):  # max op count is n-1 for n numbers
        for nums in product(allowed_numbers, repeat=op_count + 1):
            for ops in product(operators, repeat=op_count):
                result = evaluate_expression(nums, ops)
                expression = ' '.join(f'{n} {o}' for n, o in zip(nums, ops + ('',)))
                print(f"Trying: {expression}")

                if result == target:
                    print(f"Found valid solution {expression} = {target}")
                    if op_count < min_operators:
                        min_operators = op_count
                        solutions = [(nums, ops)]
                        break
                    elif op_count == min_operators:
                        solutions.append((nums, ops))

            # Exit if a solution is found
            if min_operators != float('inf'):
                break

        # Early exit if a solution is found
        if min_operators != float('inf'):
            break

    print(f"\nMinimum number of operators found: {min_operators}")
    
    # Step 2: Now find all combinations using the minimum number of operators
    best_solutions = []
    if min_operators != float('inf'):
        for nums in product(allowed_numbers, repeat=min_operators + 1):
            for ops in product(operators, repeat=min_operators):
                result = evaluate_expression(nums, ops)
                expression = ' '.join(f'{n} {o}' for n, o in zip(nums, ops + ('',)))
                print(f"Using {min_operators} operators: {expression}")

                if result == target:
                    print(f"{expression} = {target}")
                    best_solutions.append((nums, ops))

    return min_operators, best_solutions

allowed_numbers = [1, 2, 3, 4, 5, 6]
target_number = 51
min_operators, solutions = find_min_operators(allowed_numbers, target_number)

print(f"\nMinimum number of operators: {min_operators}")
for nums, ops in solutions:
    print(f"Solution: {' '.join(f'{n} {o}' for n, o in zip(nums, ops + ('',)))} = {target_number}")