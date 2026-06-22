def validate_n(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

def generate_checkerboard(n):
    validate_n(n)
    return [[(i + j) % 2 for j in range(n)] for i in range(n)]

if __name__ == '__main__':
    try:
        n1 = 3
        result1 = generate_checkerboard(n1)
        print(f"Checkerboard for n={n1}:")
        for row in result1:
            print(row)
        n2 = 4
        result2 = generate_checkerboard(n2)
        print(f"\nCheckerboard for n={n2}:")
        for row in result2:
            print(row)
    except ValueError as e:
        print(e)