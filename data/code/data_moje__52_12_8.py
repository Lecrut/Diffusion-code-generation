import sys

def print_diamond(radius):
    if radius <= 0:
        return ""
    lines = []
    for i in range(1, radius + 1):
        spaces = ' ' * (radius - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    for i in range(radius - 1, 0, -1):
        spaces = ' ' * (radius - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    radius = 5
    result = print_diamond(radius)
    print(result)