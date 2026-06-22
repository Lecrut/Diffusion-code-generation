def hollow_equilateral_triangle(height):
    if height <= 0:
        return ""
    lines = []
    for i in range(height):
        width = 2 * height - 1
        if i == 0:
            line = ' ' * (height - 1 - i) + '*' + ' ' * (2 * i - 1).replace(' ', ' ') if i > 0 else '*'
            if i == 0:
                line = ' ' * (height - 1) + '*'
        elif i == height - 1:
            line = '*' * (2 * i + 1)
        else:
            line = ' ' * (height - 1 - i) + '*' + ' ' * (2 * i - 1) + '*'
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = hollow_equilateral_triangle(5)
    print(result)