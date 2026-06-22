def generate_hollow_triangle(size):
    if size < 1:
        return []
    result = []
    for i in range(size):
        if i == 0:
            result.append('* ' * (size - i + (size - 1))[:size].strip() + ' ' * (size - i - 1))
        elif i == size - 1:
            result.append('* ' * size)
        else:
            stars = '*' + ' ' * (2 * i - 1) + '*'
            result.append(stars)
    if size == 1:
        return ['*']
    lines = []
    for i in range(size):
        if i == 0:
            spaces = ' ' * (size - 1 - i)
            lines.append(spaces + '*')
        elif i == size - 1:
            star_row = '* ' * size
            lines.append(star_row.strip())
        else:
            left_spaces = ' ' * (size - 1 - i)
            middle_spaces = ' ' * (2 * i - 1)
            lines.append(left_spaces + '*' + middle_spaces + '*')
    return lines
if __name__ == '__main__':
    for line in generate_hollow_triangle(5):
        print(line)