def right_aligned_pyramid(rows=8):
    max_width = 2 * rows - 1
    for i in range(1, rows + 1):
        stars = '*' * (2 * i - 1)
        padding = ' ' * (max_width - (2 * i - 1))
        yield padding + stars

if __name__ == '__main__':
    result = list(right_aligned_pyramid())
    for line in result:
        print(line)