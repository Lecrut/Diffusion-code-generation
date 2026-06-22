def build_symmetric_pyramid(rows: int) -> list:
    max_number_width = len(str(rows))
    padding_pattern = []
    for r in range(rows):
        spaces = rows - r - 1
        padding_pattern.append(" " * spaces)
    
    pyramid = []
    for r in range(rows):
        current_row = []
        current_row.append(padding_pattern[r])
        left_nums = list(range(1, r + 1))
        right_nums = list(range(r, 0, -1))
        all_nums = left_nums + right_nums
        num_strs = [str(n).rjust(max_number_width) for n in all_nums]
        row_str = " ".join(num_strs)
        if r > 0:
            row_str = row_str + " " + padding_pattern[r].strip()
        pyramid.append(row_str)
    return pyramid

if __name__ == '__main__':
    sample_rows = 6
    result = build_symmetric_pyramid(sample_rows)
    for line in result:
        print(line)