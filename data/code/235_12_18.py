def validate_input(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

def generate_pyramid_line_pattern(n):
    validate_input(n)
    pattern = "\n".join(["*" * (2 * i - 1) for i in range(1, n + 1)])
    return pattern

if __name__ == '__main__':
    sample_number = 5
    result = generate_pyramid_line_pattern(sample_number)
    print(result)