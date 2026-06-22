def draw_diamond(n):
    for i in range(2 * n - 1):
        spaces = abs(i - (n - 1))
        bars = 2 * (n - spaces) - 1
        print(' ' * spaces + '|' * bars)

if __name__ == '__main__':
    draw_diamond(5)