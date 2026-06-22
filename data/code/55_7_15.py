def reverse_alphabet_triangle(start_char, end_char):
    start_ord = ord(start_char)
    end_ord = ord(end_char)
    if start_ord > end_ord:
        start_ord, end_ord = end_ord, start_ord
    result_lines = []
    for current_ord in range(start_ord, end_ord + 1):
        char = chr(current_ord)
        result_lines.append(char * (current_ord - start_ord + 1))
    return '\n'.join(result_lines)

if __name__ == '__main__':
    start_val = 'A'
    end_val = 'E'
    print(reverse_alphabet_triangle(start_val, end_val))