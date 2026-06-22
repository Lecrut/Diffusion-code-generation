def generate_diamond(n):
    if n % 2 == 0:
        raise ValueError("Input must be an odd number")
    
    middle = (n + 1) // 2
    
    for i in range(n):
        spaces = abs(middle - i - 1)
        stars = n - spaces * 2
        print(" " * spaces + "*" * stars)

if __name__ == '__main__':
    try:
        generate_diamond(5)
    except ValueError as e:
        print(e)