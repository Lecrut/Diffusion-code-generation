def generate_right_aligned_pyramid(rows=5):
    lines = []
    for i in range(1, rows + 1):
        line = ' ' * (rows - i) + str(i) * i
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_right_aligned_pyramid(5)
    print(result)