def right_aligned_number_pyramid_chunk_generator(rows=8):
    max_width = len(str(rows * rows)) + 2 * (rows - 1)
    for i in range(1, rows + 1):
        line_numbers = []
        current_val = 1
        for j in range(i):
            line_numbers.append(str(current_val))
            current_val += 1
        line_content = '  '.join(line_numbers)
        padded_line = line_content.rjust(max_width) + '\n'
        yield padded_line

if __name__ == '__main__':
    chunks = list(right_aligned_number_pyramid_chunk_generator(8))
    print(''.join(chunks), end='')