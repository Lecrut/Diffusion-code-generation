def print_square_box(size):
    HASH_PATTERN = '#' * size
    for _ in range(size):
        print(HASH_PATTERN)

if __name__ == '__main__':
    print_square_box(4)