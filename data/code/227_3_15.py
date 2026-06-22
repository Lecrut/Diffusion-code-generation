def print_diamond(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    middle = n // 2
    for i in range(n):
        spaces = abs(middle - i)
        stars = n - 2 * spaces
        print(" " * spaces + "*" * stars)

if __name__ == '__main__':
    try:
        n_value = 5
        print_diamond(n_value)
    except ValueError as e:
        print(e)