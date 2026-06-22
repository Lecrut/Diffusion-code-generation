def print_star_square(size):
    if size <= 0:
        return
    full_row = "*" * size
    if size == 1:
        print(full_row)
        return
    inner_space = " " * (size - 2)
    hollow_row = "*" + inner_space + "*"
    print(full_row)
    for _ in range(size - 2):
        print(hollow_row)
    print(full_row)

if __name__ == '__main__':
    test_size = 7
    print_star_square(test_size)
    print()
    print_star_square(2)
    print()
    print_star_square(12)