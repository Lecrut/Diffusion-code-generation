def print_alphabet_triangle():
    char_code = 65
    for i in range(5):
        line = ""
        for j in range(i + 1):
            line += chr(char_code + j)
        print(line)

if __name__ == '__main__':
    print_alphabet_triangle()