def hollow_square(n):
    if n <= 0: return ''
    top_bottom = '*' * n
    middle = '*' + ' ' * (n - 2) + '*' if n > 1 else ''
    return '\n'.join([top_bottom] + [middle] * (n - 2) + [top_bottom] if n > 1 else [top_bottom])

if __name__ == '__main__':
    print(hollow_square(5))