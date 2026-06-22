def generate_symmetric_pyramid(levels):
    result = []
    max_width = (levels * 2) - 1
    
    for i in range(1, levels + 1):
        num = i
        row_nums = [str(num)] * i
        center_part = "".join(row_nums)
        remaining_width = max_width - len(center_part)
        left_pad = " " * (remaining_width // 2)
        right_pad = " " * (remaining_width // 2)
        line = left_pad + center_part + right_pad
        result.append(line)
        
    return "\n".join(result)

if __name__ == '__main__':
    num_levels = 4
    output = generate_symmetric_pyramid(num_levels)
    print(output)