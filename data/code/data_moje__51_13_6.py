def generate_symmetric_pyramid(rows):
    results = []
    max_width = 2 * rows - 1
    for i in range(1, rows + 1):
        num_str = str(i)
        current_row_width = 2 * i - 1
        padding = (max_width - current_row_width) // 2
        row_content = ' '.join(str(j) for j in range(1, i + 1))
        reversed_part = ' '.join(str(j) for j in range(i - 1, 0, -1))
        full_number_part = f"{row_content} {reversed_part}" if i > 1 else row_content
        line = ' '.join([' '] * padding) + full_number_part + ' '.join([' '] * padding)
        results.append(line.rstrip())
    return '\n'.join(results)

if __name__ == '__main__':
    print(generate_symmetric_pyramid(8))