def render_diamond(size: int = 3) -> list[str]:
    upper = [
        ' ' * (size - i - 1) + '*' * (2 * i + 1)
        for i in range(size)
    ]
    lower = [
        ' ' * (j) + '*' * (2 * (size - 1 - j) + 1)
        for j in range(size - 1, 0, -1)
    ]
    return upper + lower

if __name__ == '__main__':
    SIZE = 3
    result = render_diamond(SIZE)
    for line in result:
        print(line)