def print_square_box(size):
    line = '#' * size
    for _ in range(size):
        print(line)

if __name__ == '__main__':
    box_size = 4
    print_square_box(box_size)