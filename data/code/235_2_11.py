def draw_diamond():
    rows = 5
    for i in range(rows):
        spaces = ' ' * (rows - i - 1)
        bars = '*' * (2 * i + 1)
        print(spaces + bars)

if __name__ == '__main__':
    draw_diamond()