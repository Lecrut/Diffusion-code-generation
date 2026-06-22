def print_star_square(rows, cols):
    line = '*' * cols
    for _ in range(rows):
        print(line)

if __name__ == '__main__':
    print_star_square(6, 6)