def generate_symmetric_pyramid(n):
    lines = []
    max_width = 2 * n - 1
    for i in range(1, n + 1):
        number = i
        num_str = str(number)
        digits_count = len(num_str)
        
        left_space_count = n - i
        left_space = ' ' * left_space_count
        
        right_space_count = left_space_count
        right_space = ' ' * right_space_count
        
        left_part_nums = []
        current = i
        while current > 0:
            left_part_nums.append(str(current))
            current -= 1
        
        right_part_nums = []
        current = 1
        while current < i:
            right_part_nums.append(str(current))
            current += 1
            
        if i == 1:
            middle_part = []
        else:
            middle_part = [str(i)]
            
        full_line_parts = [left_space] + left_part_nums + middle_part + right_part_nums + [right_space]
        line = ''.join(full_line_parts)
        lines.append(line)
        
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_symmetric_pyramid(8)
    print(result)