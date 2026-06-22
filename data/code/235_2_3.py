def draw_diamond(n):
    for i in range(2 * n - 1):
        spaces = abs(n - i - 1)
        bars = 2 * min(i, n - i) + 1
        print(' ' * spaces + '|' * bars)

if __name__ == '__main__':
    draw_diamond(5)