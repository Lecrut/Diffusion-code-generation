def generate_right_aligned_pyramid(rows):
    for i in range(1, rows + 1):
        line_numbers = " ".join(str(num) for num in range(1, i + 1))
        total_width = len(" ".join(str(num) for num in range(1, rows + 1)))
        padded_line = line_numbers.rjust(total_width)
        yield padded_line

if __name__ == '__main__':
    for chunk in generate_right_aligned_pyramid(8):
        print(chunk)