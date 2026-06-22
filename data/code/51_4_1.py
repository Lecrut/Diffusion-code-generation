def generate_number_pyramid(rows):
    lines = []
    max_width = rows + rows - 1
    for i in range(1, rows + 1):
        num_str = ' '.join(str(j) for j in range(1, i + 1))
        padding = (max_width - len(num_str.replace(' ', ''))) // 2
        padded_line = ' ' * padding + num_str
        lines.append(padded_line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_number_pyramid(3)
    print(result)