CHECKERBOARD_PATTERN = 2

def generate_checkerboard(n):
    return [[(i + j) % CHECKERBOARD_PATTERN for j in range(n)] for i in range(n)]

if __name__ == '__main__':
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