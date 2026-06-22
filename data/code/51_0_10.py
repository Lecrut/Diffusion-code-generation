def generate_right_aligned_pyramid(rows=5):
    lines = []
    for i in range(1, rows + 1):
        line = ' ' * (rows - i) + ''.join(str(j) for j in range(1, i + 1))
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_right_aligned_pyramid())