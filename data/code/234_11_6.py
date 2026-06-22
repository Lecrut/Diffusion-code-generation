def generate_checkerboard(n):
    return [[(i + j) % 2 for j in range(n)] for i in range(n)]

if __name__ == '__main__':
    n1 = 5
    result1 = generate_checkerboard(n1)
    print(f"Checkerboard for n={n1}:")
    for row in result1:
        print(row)