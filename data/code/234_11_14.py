def create_checkerboard(N):
    return [[(i + j) % 2 for j in range(N)] for i in range(N)]

if __name__ == '__main__':
    print(create_checkerboard(4))