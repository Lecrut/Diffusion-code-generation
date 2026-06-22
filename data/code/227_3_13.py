def print_diamond(n):
    if not isinstance(n, int) or n % 2 == 0 or n < 1:
        raise ValueError("Input must be an odd integer greater than 0")
    
    middle = (n + 1) // 2
    
    for i in range(n):
        spaces = abs(middle - i - 1)
        stars = 2 * min(i, n - i) + 1
        print(" " * spaces + "*" * stars)

if __name__ == '__main__':
    print_diamond(5)