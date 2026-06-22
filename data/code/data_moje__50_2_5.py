def generate_centered_triangle(star, size):
    lines = []
    for i in range(1, size + 1):
        spaces = size - i
        stars = 2 * i - 1
        line = ' ' * spaces + star * stars
        lines.append(line)
    return lines

if __name__ == '__main__':
    result = generate_centered_triangle('*', 12)
    for line in result:
        print(line)