def generate_pyramid(base_width):
    if base_width < 1 or base_width % 2 == 0:
        return []
    
    lines = []
    for i in range(1, base_width + 1, 2):
        padding = (base_width - i) // 2
        row = ' ' * padding + '*' * i
        lines.append(row)
    return lines

if __name__ == '__main__':
    result = generate_pyramid(21)
    for line in result:
        print(line)