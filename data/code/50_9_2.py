def get_inverted_triangle(height):
    lines = []
    for i in range(height):
        stars = (height - i) * 2 - 1
        line = '*' * stars
        lines.append(line)
    result = '\n'.join(lines)
    return result

if __name__ == '__main__':
    height = 5
    print(get_inverted_triangle(height))