def generate_number_pyramid(rows):
    max_width = len(str(rows * 2 - 1))
    lines = []
    for i in range(1, rows + 1):
        numbers = [str(j) for j in range(1, i + 1)] + [str(j) for j in range(i - 1, 0, -1)]
        line = ''.join(numbers)
        padded = line.center(max_width)
        lines.append(padded)
    return lines

if __name__ == '__main__':
    pyramid_lines = generate_number_pyramid(7)
    for line in pyramid_lines:
        print(line)