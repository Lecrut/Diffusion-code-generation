def build_number_pyramid():
    level = 6
    numbers = [str((i + 1) * (level - abs(j - level + 1))) for i in range(level) for j in range(level - abs(i - level + 1))]
    rows = []
    for i in range(level):
        width = 2 * level - 1
        count = 2 * i + 1
        current_nums = []
        for j in range(count):
            val = (i + 1) * (i + 1) + j
            current_nums.append(str(val))
        row_str = ' '.join(current_nums).center(width).strip()
        rows.append(row_str)
    size = 6
    result = []
    current_number = 1
    max_width = 2 * size - 1
    for i in range(size):
        row_numbers = []
        for j in range(i + 1):
            row_numbers.append(str(current_number))
            current_number += 1
        row_str = ' '.join(row_numbers)
        padded_row = row_str.center(max_width)
        result.append(padded_row)
    return result
if __name__ == '__main__':
    pyramid = build_number_pyramid()
    for line in pyramid:
        print(line)