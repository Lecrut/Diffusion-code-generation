def generate_number_pyramid(rows):
    max_width = 2 * rows - 1
    lines = [
        ' ' * (rows - i - 1) + ''.join(str((j % (2 * i)) + 1 if j % 2 == 0 else ' ' for j in range(2 * i + 1)))
        for i in range(1, rows + 1)
    ]
    center_pad = max(len(line) for line in lines)
    centered_lines = [line.center(center_pad) for line in lines]
    return '\n'.join(centered_lines)

if __name__ == '__main__':
    result = generate_number_pyramid(7)
    print(result)