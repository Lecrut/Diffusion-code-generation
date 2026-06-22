def print_diamond(size: int) -> list[str]:
    lines: list[str] = []
    for i in range(size):
        spaces = abs(size // 2 - i)
        stars = size - 2 * spaces
        line = ' ' * spaces + '* ' * stars
        lines.append(line.rstrip())
    return lines

if __name__ == '__main__':
    size = 8
    result = print_diamond(size)
    for line in result:
        print(line)