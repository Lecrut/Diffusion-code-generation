def square(n):
    return '\n'.join(('#' * n if i in (0, n - 1) else '#' + ' ' * (n - 2) + '#') for i in range(n)) if n > 1 else ''

if __name__ == '__main__':
    print(square(5))