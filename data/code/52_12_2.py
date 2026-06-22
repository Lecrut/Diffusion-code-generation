def generate_diamond(radius):
    lines = []
    for i in range(-radius, radius + 1):
        abs_i = abs(i)
        spaces = radius - abs_i
        stars = 2 * abs_i + 1
        line = ' ' * spaces + '*' * stars
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    radius = 3
    result = generate_diamond(radius)
    print(result)