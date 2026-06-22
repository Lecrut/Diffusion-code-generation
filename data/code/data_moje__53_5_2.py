def generate_symmetric_reverse_triangle(rows):
    result = []
    for i in range(1, rows + 1):
        row_nums = list(range(i, 0, -1))
        padding = ' ' * (rows - i)
        left_part = ' '.join(str(n) for n in row_nums)
        right_part = ' '.join(str(n) for n in row_nums[:-1][::-1])
        if right_part:
            full_line = padding + left_part + ' ' + right_part
        else:
            full_line = padding + left_part
        result.append(full_line)
    return result

if __name__ == '__main__':
    lines = generate_symmetric_reverse_triangle(5)
    for line in lines:
        print(line)