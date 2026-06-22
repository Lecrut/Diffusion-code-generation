def draw_diamond(rows):
    for i in range(2 * rows - 1):
        spaces = abs(i - (rows - 1))
        bars = 2 * (rows - spaces) - 1
        print(' ' * spaces + '|' * bars)

if __name__ == '__main__':
    draw_diamond(5)