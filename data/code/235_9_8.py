def generate_line_pattern(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    pattern = ""
    for i in range(n):
        pattern += "*" * (2 * i + 1) + "\n"
    return pattern

if __name__ == '__main__':
    try:
        sample_output = generate_line_pattern(5)
        print(sample_output)
    except ValueError as e:
        print(e)