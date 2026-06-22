def reverse_triangle(start_char, end_char):
    if ord(start_char) > ord(end_char):
        start_char, end_char = end_char, start_char
    if len(start_char) != 1 or len(end_char) != 1:
        raise ValueError("Start and end must be single characters")
    if not ('A' <= start_char <= 'Z' and 'A' <= end_char <= 'Z'):
        raise ValueError("Characters must be uppercase letters")
    
    start_code = ord(start_char)
    end_code = ord(end_char)
    char_range = list(range(start_code, end_code + 1))
    char_range.reverse()
    
    result_lines = []
    row_len = len(char_range)
    for i in range(row_len):
        chars_to_print = char_range[:i + 1]
        line = "".join(chr(c) for c in chars_to_print)
        result_lines.append(line)
    
    return "\n".join(result_lines)

if __name__ == '__main__':
    print(reverse_triangle('A', 'E'))