def generate_diamond(size):
    if size <= 0:
        return []
    if size % 2 == 0:
        half = size // 2
    else:
        half = size // 2
    top_lines = []
    for i in range(half, -1, -1):
        spaces = ' ' * i
        stars = '*' * (size - 2 * i)
        top_lines.append(spaces + stars + spaces)
    bottom_lines = top_lines[:-1][::-1]
    if size % 2 == 0:
        return top_lines + bottom_lines
    return top_lines + bottom_lines

if __name__ == '__main__':
    result = generate_diamond(5)
    for line in result:
        print(line)