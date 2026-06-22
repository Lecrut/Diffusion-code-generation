def generate_checkerboard(n):
    return [[(i + j) % 2 for j in range(n)] for i in range(n)]

if __name__ == '__main__':
    n3 = 5
    result3 = generate_checkerboard(n3)
    print(f"Checkerboard for n={n3}:")
    for row in result3:
        print(row)
    
    n4 = 6
    result4 = generate_checkerboard(n4)
    print(f"\nCheckerboard for n={n4}:")
    for row in result4:
        print(row)