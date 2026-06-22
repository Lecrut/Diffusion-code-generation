def validate_input(start, step, n):
    if not isinstance(start, (int, float)) or start < 1:
        raise ValueError("Start value must be a positive number")
    if not isinstance(step, int) or step <= 0:
        raise ValueError("Step size must be a positive integer")
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Number of steps must be a positive integer")

def print_incremental_sequence(start, step, n):
    current_value = start
    for _ in range(n):
        print(current_value)
        current_value += step

if __name__ == '__main__':
    validate_input(1, 1, 5)
    print_incremental_sequence(1, 1, 5)