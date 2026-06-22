if __name__ == '__main__':
    size = 10
    checkerboard = [[(i + j) % 2 for i in range(size)] for j in range(size)]
    print(checkerboard)