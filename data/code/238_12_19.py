def render_diamond():
    size = 7
    for i in range(size):
        if i < size // 2 + 1:
            print(' ' * (size // 2 - i) + '+' * (2 * i + 1))
        else:
            print(' ' * (i - size // 2) + '+' * (2 * (size - i) - 1))

if __name__ == '__main__':
    render_diamond()