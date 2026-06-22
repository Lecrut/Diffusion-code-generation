def reverse_alphabet_triangle(start_char='Z', end_char='A'):
    start_ord = ord(start_char)
    end_ord = ord(end_char)
    if start_ord < end_ord:
        raise ValueError("Start character must be greater than or equal to end character in alphabet order")
    
    chars = []
    current_ord = start_ord
    while current_ord >= end_ord:
        chars.append(chr(current_ord))
        current_ord -= 1
    
    lines = []
    n = len(chars)
    for i in range(n):
        line_chars = []
        for j in range(i + 1):
            line_chars.append(chars[j])
        lines.append(" ".join(line_chars))
    
    return "\n".join(lines)

if __name__ == '__main__':
    result = reverse_alphabet_triangle()
    print(result)