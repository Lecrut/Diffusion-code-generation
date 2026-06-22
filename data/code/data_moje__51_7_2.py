def generate_right_aligned_pyramid(rows=8):
    max_width = rows * 2 - 1
    for i in range(1, rows + 1):
        num_str = str(i)
        line_content = (num_str + ' ') * (i - 1) + num_str
        padding = ' ' * (max_width - len(line_content))
        yield padding + line_content + '\n'

if __name__ == '__main__':
    result_chunks = list(generate_right_aligned_pyramid(8))
    print(''.join(result_chunks), end='')