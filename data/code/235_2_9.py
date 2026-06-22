def draw_diamond(n):
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        bars = '|' * (2 * i + 1)
        print(spaces + bars)

if __name__ == '__main__':
    n = 5
    draw_diamond(n)