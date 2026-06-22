def create_checkerboard(size):
    return [[(i + j) % 2 for j in range(size)] for i in range(size)]

if __name__ == '__main__':
    checkerboard = create_checkerboard(10)
    print(checkerboard)