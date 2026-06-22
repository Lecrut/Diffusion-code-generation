def generate_number_pyramid(row_count):
    lines = []
    for i in range(1, row_count + 1):
        left_part = []
        for j in range(1, i):
            left_part.append(str(j))
        current_row = ''.join(left_part) + str(i) + ''.join(reversed(left_part))
        spacing = ' ' * (row_count - i)
        lines.append(spacing + current_row + spacing)
    return lines

if __name__ == '__main__':
    result = generate_number_pyramid(8)
    for line in result:
        print(line)