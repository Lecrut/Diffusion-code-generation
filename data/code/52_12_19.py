def make_diamond(r):
    return '\n'.join(' ' * (r - i) + '*' * (2 * i - 1) if 1 <= i <= r else ' ' * (i - r) + '*' * (2 * (2 * r - i) - 1) if r < i <= 2 * r - 1 else '' for i in range(1, 2 * r))

if __name__ == '__main__':
    print(make_diamond(5))