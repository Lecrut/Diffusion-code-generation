def generate_hollow_square(size):
    if size <= 0:
        return ''
    if size == 1:
        return '*'
    result = []
    top_bottom = '* ' * size
    top_row = '*' * size
    result.append(top_row)
    for _ in range(size - 2):
        inner = '*' + ' ' * (size - 2) + '*'
        result.append(inner)
    if size > 1:
        result.append(top_row)
    return '\n'.join(result)
if __name__ == '__main__':
    print(generate_hollow_square(5))
    print('')
    print(generate_hollow_square(4))
    print('')
    print(generate_hollow_square(1))
    print('')
    print(generate_hollow_square(0))