def print_star_square(size):
    star_line = "*" * size
    for _ in range(size):
        print(star_line)

if __name__ == '__main__':
    print_star_square(6)