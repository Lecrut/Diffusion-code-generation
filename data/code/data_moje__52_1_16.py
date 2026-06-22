def print_diamond(height: int=7) -> str:
    if height % 2 == 0:
        raise ValueError('Height must be an odd number.')
    middle = height // 2
    lines = []
    for i in range(height):
        if i <= middle:
            spaces = middle - i
            stars = 2 * i + 1
        else:
            spaces = i - middle
            stars = 2 * (height - 1 - i) + 1
        line = ' ' * spaces + '*' * stars
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    result = print_diamond(7)
    print(result)