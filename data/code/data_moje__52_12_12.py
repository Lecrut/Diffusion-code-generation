def draw_diamond(radius: int) -> str:
    lines = []
    for i in range(-radius, radius + 1):
        spaces = abs(i)
        stars = 2 * (radius - spaces) + 1
        lines.append(' ' * spaces + '*' * stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = draw_diamond(4)
    print(result)