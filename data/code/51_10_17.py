def generate_number_pyramid(height):
    pyramid_lines = []
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        numbers = ' '.join((str((i + j) % 10 if (i + j) % 10 != 0 else 10) for j in range(2 * i - 1)))
        row_numbers = [str(i - j) for j in range(i)]
        row_str = ' '.join(row_numbers)
        max_width = 2 * height - 1
        padded_row = row_str.center(max_width)
        pyramid_lines.append(padded_row)
    return '\n'.join(pyramid_lines)
if __name__ == '__main__':
    height = 5
    pyramid = generate_number_pyramid(height)
    print(pyramid)