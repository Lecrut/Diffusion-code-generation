def generate_diamond_pattern(size):
    if size <= 0:
        return []
    lines = []
    for i in range(1, size + 1):
        stars = 2 * i - 1
        spaces = size - i
        line = ' ' * spaces + '*' * stars + ' ' * spaces
        lines.append(line)
    for i in range(size - 1, 0, -1):
        stars = 2 * i - 1
        spaces = size - i
        line = ' ' * spaces + '*' * stars + ' ' * spaces
        lines.append(line)
    return lines

def print_diamond_pattern(size):
    lines = generate_diamond_pattern(size)
    for line in lines:
        print(line)
if __name__ == '__main__':
    size = 5
    diamond_lines = generate_diamond_pattern(size)
    for line in diamond_lines:
        print(line)