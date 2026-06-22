def generate_right_aligned_pyramid(rows):
    result = []
    for current_row in range(1, rows + 1):
        spaces = rows - current_row
        numbers = ' '.join(str(i) for i in range(1, current_row + 1))
        line = ' ' * spaces + numbers
        result.append(line)
    return result

if __name__ == '__main__':
    pyramid_lines = generate_right_aligned_pyramid(5)
    for line in pyramid_lines:
        print(line)