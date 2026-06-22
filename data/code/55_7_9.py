def reverse_triangle_pattern(start_char, end_char):
    start_code = ord(start_char)
    end_code = ord(end_char)
    if start_code < end_code:
        return ""
    
    chars = []
    current = start_code
    while current >= end_code:
        chars.append(chr(current))
        current -= 1
    
    result_lines = []
    for i in range(len(chars)):
        line = chars[-(i + 1)] * (i + 1)
        result_lines.append(line)
    
    return "\n".join(result_lines)

if __name__ == '__main__':
    start = 'M'
    end = 'A'
    output = reverse_triangle_pattern(start, end)
    print(output)