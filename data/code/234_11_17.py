def create_checkerboard(N):
    return [[(i + j) % 2 for j in range(N)] for i in range(N)]

if __name__ == '__main__':
    n = 5
    checkerboard = create_checkerboard(n)
    print(f"Checkerboard for n={n}:")
    for row in checkerboard:
        print(row)