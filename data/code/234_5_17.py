import itertools
CHECKERBOARD_SIZE = 8

def create_checkerboard(size=CHECKERBOARD_SIZE):
    return [[(i + j) % 2 for j in range(size)] for i in range(size)]
if __name__ == '__main__':
    size = CHECKERBOARD_SIZE
    checkerboard = create_checkerboard(size)
    print(checkerboard)