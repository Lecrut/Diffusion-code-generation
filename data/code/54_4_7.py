def construct_hollow_square(size=10):
    border = '*' * size
    hollow = '*' + ' ' * (size - 2) + '*'
    lines = [border] + [hollow] * (size - 2) + [border]
    return '\n'.join(lines)

if __name__ == '__main__':
    result = construct_hollow_square(10)
    print(result)