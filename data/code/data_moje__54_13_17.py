def make_hollow_square(size: int) -> str:
    if size <= 0:
        return ''
    if size == 1:
        return '*'
    top_bottom = '*' * size
    middle = '*' + ' ' * (size - 2) + '*'
    return '\n'.join([top_bottom] + [middle] * (size - 2) + [top_bottom])

if __name__ == '__main__':
    print(make_hollow_square(6))