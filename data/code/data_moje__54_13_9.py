def hollow_square(n):
    return '\n'.join(['*' * n if i == 0 or i == n - 1 else '*' + ' ' * (n - 2) + '*' if n > 1 else '*' for i in range(n)]) if n > 0 else ''

if __name__ == '__main__':
    print(hollow_square(5))