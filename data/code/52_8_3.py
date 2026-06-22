def generate_diamond_star_pattern(height=7):
    if height % 2 == 0:
        height += 1
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
    result = generate_diamond_star_pattern(7)
    print(result)