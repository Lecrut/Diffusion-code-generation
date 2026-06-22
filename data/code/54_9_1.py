def hollow_square(rows, cols):
    for r in range(rows):
        if r == 0 or r == rows - 1:
            yield '#' * cols
        else:
            if cols > 1:
                yield '#' + ' ' * (cols - 2) + '#'
            else:
                yield '#'

if __name__ == '__main__':
    for row in hollow_square(5, 7):
        print(row)