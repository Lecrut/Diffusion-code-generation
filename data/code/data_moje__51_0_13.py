def generate_right_aligned_pyramid(rows):
    result = []
    for i in range(1, rows + 1):
        line_numbers = list(range(1, i + 1))
        line_str = ' '.join(map(str, line_numbers))
        max_width = (rows * 2) - 1
        padded_line = line_str.rjust(max_width)
        result.append(padded_line)
    return '\n'.join(result)

if __name__ == '__main__':
    ROWS = 5
    output = generate_right_aligned_pyramid(ROWS)
    print(output)