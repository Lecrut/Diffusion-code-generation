def validate_size(size):
    if size <= 0:
        raise ValueError("Size must be greater than 0")

def print_square_box(size):
    validate_size(size)
    pattern = '#' * size
    for _ in range(size):
        print(pattern)

if __name__ == '__main__':
    print_square_box(4)