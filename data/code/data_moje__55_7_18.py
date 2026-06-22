def reverse_alphabet_triangle():
    start_char = 'z'
    end_char = 'a'
    start_ord = ord(start_char)
    end_ord = ord(end_char)
    
    if start_ord < end_ord:
        start_ord, end_ord = end_ord, start_ord
        
    chars = [chr(i) for i in range(start_ord, end_ord - 1, -1)]
    
    result = []
    current_row = 1
    while current_row <= len(chars):
        row_chars = []
        for i in range(current_row):
            row_chars.append(chars[i])
        result.append(" ".join(row_chars))
        current_row += 1
        
    return "\n".join(result)

if __name__ == '__main__':
    print(reverse_alphabet_triangle())