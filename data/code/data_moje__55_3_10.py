def generate_inverted_alphabet_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        line = ""
        for j in range(i):
            char_code = 65 + j
            line += chr(char_code)
        result.append(line)
    return result

if __name__ == '__main__':
    sample_rows = 5
    output = generate_inverted_alphabet_triangle(sample_rows)
    for line in output:
        print(line)