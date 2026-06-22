import itertools

def construct_checkerboard(size):
    return [[(i + j) % 2 for j in range(size)] for i in range(size)]

if __name__ == '__main__':
    size = 8
    checkerboard = construct_checkerboard(size)
    print(checkerboard)