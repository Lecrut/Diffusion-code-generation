def generate_alphabet_triangle():
    rows = 26
    result = []
    for i in range(1, rows + 1):
        line = ""
        for j in range(i):
            char_code = ord('A') + j
            line += chr(char_code)
        result.append(line)
    return "\n".join(result)

if __name__ == '__main__':
    print(generate_alphabet_triangle())