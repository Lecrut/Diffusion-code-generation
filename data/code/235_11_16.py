def render_diamond(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    for i in range(n-2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

if __name__ == '__main__':
    diamond_height = 7
    render_diamond(diamond_height)