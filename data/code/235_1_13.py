def validate_size(size):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")

def print_square_box(size):
    validate_size(size)
    pattern = '#' * size
    for _ in range(size):
        print(pattern)

if __name__ == '__main__':
    print_square_box(4)