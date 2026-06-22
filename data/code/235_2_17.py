def draw_diamond():
    for i in range(3):
        print(' ' * (2 - i) + '|' * (2 * i + 1))
    for i in range(3, 0, -1):
        print(' ' * (2 - i) + '|' * (2 * i + 1))

if __name__ == '__main__':
    draw_diamond()