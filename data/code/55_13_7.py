def print_alphabet_triangle(rows):
    for i in range(1, rows + 1):
        char_code = ord('A')
        line = ""
        for j in range(i):
            line += chr(char_code)
            char_code += 1
        print(line)

if __name__ == '__main__':
    sample_rows = 5
    print_alphabet_triangle(sample_rows)