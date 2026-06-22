def generate_symmetric_pyramid(rows: int) -> str:
    max_width = 2 * rows - 1
    result = []
    for i in range(1, rows + 1):
        center_pos = rows
        num_val = i
        left_spacer = ' ' * (center_pos - i)
        right_spacer = ' ' * (center_pos - i)
        nums = []
        for j in range(1, num_val + 1):
            nums.append(str(j))
        for j in range(num_val - 1, 0, -1):
            nums.append(str(j))
        row_str = left_spacer + ' '.join(nums) + right_spacer
        result.append(row_str)
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_symmetric_pyramid(8))