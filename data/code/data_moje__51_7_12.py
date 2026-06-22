def generate_right_aligned_pyramid():
    def get_row_text(row_index, total_rows):
        width = total_rows
        current_row_str = ''
        for k in range(1, row_index + 1):
            val = k
            val_str = str(val)
            padding = ' ' * (width - len(val_str) - len(current_row_str.strip()) // 2)
            current_row_str += padding + val_str
        max_width = total_rows * 2 - 1
        return current_row_str.rjust(max_width)

    total_rows = 8
    for i in range(1, total_rows + 1):
        yield get_row_text(i, total_rows)

if __name__ == '__main__':
    result = list(generate_right_aligned_pyramid())
    print(result)