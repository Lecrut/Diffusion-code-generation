def validate_input(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

def generate_line_pattern(n):
    for i in range(n):
        print("*" * (2 * i + 1))

if __name__ == '__main__':
    sample_value = 5
    validate_input(sample_value)
    generate_line_pattern(sample_value)