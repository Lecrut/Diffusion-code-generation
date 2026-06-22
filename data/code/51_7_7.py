def right_aligned_pyramid(rows=8):
    max_width = 2 * rows - 1
    for i in range(1, rows + 1):
        spaces = ' ' * (max_width - (2 * i - 1))
        stars = '*' * (2 * i - 1)
        yield spaces + stars

if __name__ == '__main__':
    for chunk in right_aligned_pyramid():
        print(chunk)