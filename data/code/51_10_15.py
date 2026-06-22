def generate_number_pyramid(height):
    lines = []
    for i in range(1, height + 1):
        row = list(range(1, i + 1))
        row.extend(range(i - 1, 0, -1))
        max_width = (height * 2) - 1
        line = " ".join(str(num) for num in row)
        padded_line = line.center(max_width)
        lines.append(padded_line)
    return "\n".join(lines)

if __name__ == '__main__':
    height = 5
    result = generate_number_pyramid(height)
    print(result)