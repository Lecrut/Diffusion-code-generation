def generate_inverted_alphabet_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        line = ""
        for j in range(i):
            char_code = ord('A') + j
            if char_code > ord('Z'):
                char_code = ord('A') + (char_code - ord('Z') - 1)
            line += chr(char_code) + " "
        result.append(line.strip())
    return "\n".join(result)

if __name__ == '__main__':
    sample_rows = 5
    print(generate_inverted_alphabet_triangle(sample_rows))