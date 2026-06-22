def create_checkerboard(N):
    return [[(i + j) % 2 for j in range(N)] for i in range(N)]

if __name__ == '__main__':
    result4x4 = create_checkerboard(4)
    print(f"Checkerboard for n=4:")
    for row in result4x4:
        print(row)