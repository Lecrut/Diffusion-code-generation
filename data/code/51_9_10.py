def build_symmetric_pyramid(rows: int=6) -> list[str]:
    pyramid = []
    for i in range(1, rows + 1):
        left_part = list(range(1, i + 1))
        right_part = list(range(i - 1, 0, -1))
        numbers = left_part + right_part
        num_strs = [str(n) for n in numbers]
        row_content = ' '.join(num_strs)
        max_nums_in_last_row = 2 * rows - 1
        max_row_width = 2 * max_nums_in_last_row - 1
        centered_row = row_content.center(max_row_width)
        pyramid.append(centered_row)
    return pyramid
if __name__ == '__main__':
    result = build_symmetric_pyramid(6)
    print('\n'.join(result))