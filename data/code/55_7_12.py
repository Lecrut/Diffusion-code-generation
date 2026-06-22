def reverse_alpha_triangle(start_char, end_char):
    start_ord = ord(start_char)
    end_ord = ord(end_char)
    if start_ord > end_ord:
        start_ord, end_ord = end_ord, start_ord
    char_count = end_ord - start_ord + 1
    rows = char_count
    result = []
    current_char_code = end_ord
    for row_index in range(rows):
        row_chars = []
        for i in range(row_index + 1):
            if current_char_code >= start_ord:
                row_chars.append(chr(current_char_code))
                current_char_code -= 1
            else:
                row_chars.append(chr(start_ord))
        result.append(" ".join(row_chars))
    return "\n".join(result)

if __name__ == '__main__':
    start_val = 'D'
    end_val = 'Z'
    output = reverse_alpha_triangle(start_val, end_val)
    print(output)