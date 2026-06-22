def generate_right_aligned_pyramid(rows=8):
    for i in range(1, rows + 1):
        row_num = 2 ** i - 1
        row_str = str(row_num)
        yield row_str.rjust(rows * 2)

if __name__ == '__main__':
    result = list(generate_right_aligned_pyramid(8))
    print('\n'.join(result))