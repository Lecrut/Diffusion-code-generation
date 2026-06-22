def print_alphabet_triangle():
    current_char = 'A'
    row_count = 0
    max_rows = 26
    
    while row_count < max_rows and current_char <= 'Z':
        line = ''
        for i in range(row_count + 1):
            line += current_char
            current_char = chr(ord(current_char) + 1)
            if current_char > 'Z':
                break
        print(line)
        row_count += 1

if __name__ == '__main__':
    print_alphabet_triangle()