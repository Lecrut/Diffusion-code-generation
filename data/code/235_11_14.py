def render_diamond(n):
    for i in range(2 * n - 1):
        spaces = abs(n - i - 1)
        stars = 2 * min(i, n - i) + 1
        print(' ' * spaces + '*' * stars)

if __name__ == '__main__':
    render_diamond(5)