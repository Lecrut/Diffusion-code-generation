def is_even(n):
    return n % 2 == 0

def validate_input(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")

if __name__ == '__main__':
    sample_values = [10, 15, 22, 27]
    for value in sample_values:
        validate_input(value)
        print(is_even(value))