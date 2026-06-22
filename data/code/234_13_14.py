SIZE = 10

if __name__ == '__main__':
    checkerboard = [[(i + j) % 2 for i in range(SIZE)] for j in range(SIZE)]
    print(checkerboard)