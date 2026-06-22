def generate_right_aligned_pyramid(rows):
    result = []
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        numbers = str(i) * i
        result.append(spaces + numbers)
    return result

if __name__ == '__main__':
    sample_rows = 5
    pyramid_lines = generate_right_aligned_pyramid(sample_rows)
    for line in pyramid_lines:
        print(line)