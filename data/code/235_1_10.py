def print_square_box(size):
    if size < 1:
        raise ValueError("Size must be at least 1")
    
    pattern = '#' * size
    for _ in range(size):
        print(pattern)

if __name__ == '__main__':
    print_square_box(4)