def print_triangle(n):
    if n <= 0:
        return
    
    current_char_code = ord('a')
    
    for i in range(1, n + 1):
        row_chars = []
        for j in range(i):
            row_chars.append(chr(current_char_code % 26 + 97))
            current_char_code += 1
        print(' '.join(row_chars))

if __name__ == '__main__':
    print_triangle(5)