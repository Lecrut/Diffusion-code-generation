def generate_line_pattern(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    for i in range(n):
        print("*" * (2 * i + 1))

if __name__ == '__main__':
    try:
        generate_line_pattern(5)
    except ValueError as e:
        print(e)