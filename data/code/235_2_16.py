def draw_diamond(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        bars = '|' * (2 * i - 1)
        print(spaces + bars)

if __name__ == '__main__':
    diamond_height = 7
    draw_diamond(diamond_height)