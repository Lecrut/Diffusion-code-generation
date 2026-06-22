def render_diamond(size: int) -> str:
    lines = []
    for i in range(-size + 1, size):
        spaces = abs(i)
        stars = size - spaces
        lines.append(' ' * spaces + '*' * (2 * stars - 1))
    return '\n'.join(lines)

if __name__ == '__main__':
    parameter = 3
    print(render_diamond(parameter))