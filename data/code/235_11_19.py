DIAMOND_SIZE = 5

def render_diamond(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    for i in range(n-2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

if __name__ == '__main__':
    render_diamond(DIAMOND_SIZE)