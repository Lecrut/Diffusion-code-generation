def create_symmetric_number_pyramid(levels=4):
    if levels <= 0:
        return ""
    
    result_lines = []
    
    for i in range(1, levels + 1):
        spaces = ' ' * (levels - i)
        numbers = [str(j) for j in range(1, i + 1)]
        left_part = ' '.join(numbers)
        right_part = ' '.join(reversed(numbers[:-1])) if i > 1 else ""
        
        if right_part:
            line_content = left_part + ' ' + right_part
        else:
            line_content = left_part
            
        line = spaces + line_content + spaces
        result_lines.append(line)
        
    return '\n'.join(result_lines)

if __name__ == '__main__':
    output = create_symmetric_number_pyramid(4)
    print(output)