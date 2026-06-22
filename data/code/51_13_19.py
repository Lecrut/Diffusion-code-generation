def generate_symmetric_pyramid(rows):
    result = []
    for i in range(1, rows + 1):
        start_num = i * (i - 1) // 2 + 1
        end_num = i * i // 2 + i // 2
        prev_sum = (i - 1) * i // 2
        numbers = range(prev_sum + 1, prev_sum + i + 1)
        formatted_nums = [str(n).center(3) for n in numbers]
        line_content = ''.join(formatted_nums)
        max_width = 3 * rows + 2 * (rows - 1)
        slot_width = 3
        full_line = ''.join([str(n).center(slot_width) for n in numbers])
        max_len = rows * slot_width
        line = full_line.center(max_len + 2 * (rows - i))
        padding = ' ' * ((rows - i) * slot_width)
        line = padding + ''.join([str(n).center(slot_width) for n in numbers])
        result.append(line)
    return result
if __name__ == '__main__':
    pyramid_lines = generate_symmetric_pyramid(8)
    for line in pyramid_lines:
        print(line)