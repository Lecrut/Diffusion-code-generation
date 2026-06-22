import itertools

def validate_size(size):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")

def create_checkerboard(size):
    validate_size(size)
    return [[(i + j) % 2 for j in range(size)] for i in range(size)]

if __name__ == '__main__':
    size = 8
    checkerboard = create_checkerboard(size)
    print(checkerboard)