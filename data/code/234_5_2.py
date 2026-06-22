import itertools

def create_checkerboard(size):
    checkerboard = list(itertools.product(range(size), repeat=2))
    return [[int((x + y) % 2 == 0) for x, y in row] for row in checkerboard]

if __name__ == '__main__':
    size = 8
    checkerboard = create_checkerboard(size)
    print(checkerboard)