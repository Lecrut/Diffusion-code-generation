def generate_diamond_pattern(size):
    if size % 2 == 0:
        size += 1
    half = size // 2
    lines = []
    for i in range(-half, half + 1):
        spaces = ' ' * abs(i)
        stars = '*' * (size - 2 * abs(i))
        lines.append(spaces + stars + spaces)
    return lines

def print_diamond_pattern(size):
    lines = generate_diamond_pattern(size)
    for line in lines:
        print(line)
if __name__ == '__main__':
    n = 5
    result = generate_diamond_pattern(n)
    for line in result:
        print(line)