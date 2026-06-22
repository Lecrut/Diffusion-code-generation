import itertools

def create_checkerboard(size):
    return [[int((i + j) % 2 == 0) for j in range(size)] for i in range(size)]

if __name__ == '__main__':
    size = 8
    checkerboard = create_checkerboard(size)
    print(checkerboard)