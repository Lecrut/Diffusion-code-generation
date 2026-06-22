SIZE = 10

checkerboard = [[(i + j) % 2 == 1 for i in range(SIZE)] for j in range(SIZE)]

if __name__ == '__main__':
    print(checkerboard)