def render_diamond():
    size = 7
    for i in range(size):
        print(' ' * (size - i - 1) + '+' * (2 * i + 1))

if __name__ == '__main__':
    render_diamond()