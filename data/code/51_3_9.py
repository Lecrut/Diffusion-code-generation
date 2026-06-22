def print_number_pyramid(rows):
    max_width = 2 * rows - 1
    lines = [
        (" " * (max_width - (2 * i + 1)) + " ".join(map(str, range(1, i + 2))))
        .center(max_width)
        for i in range(rows)
    ]
    for line in lines:
        print(line)

if __name__ == '__main__':
    print_number_pyramid(7)