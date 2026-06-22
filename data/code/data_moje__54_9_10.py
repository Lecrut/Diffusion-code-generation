def hollow_square(rows, cols):
    if rows <= 0 or cols <= 0:
        return
    for r in range(rows):
        if r == 0 or r == rows - 1:
            yield '#' * cols
        else:
            yield '#' + ' ' * (cols - 2) + '#'

if __name__ == '__main__':
    for row in hollow_square(5, 5):
        print(row)