import itertools

def create_checkerboard(size):
    if not isinstance(size, int) or size <= 0:
        raise ValueError('Size must be a positive integer')
    coordinates = list(itertools.product(range(size), repeat=2))
    checkerboard = [[int((x + y) % 2 == 0) for x, y in row] for row in coordinates]
    return checkerboard
if __name__ == '__main__':
    size = 8
    checkerboard = create_checkerboard(size)
    print(checkerboard)