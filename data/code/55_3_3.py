def create_inverted_alphabet_triangle(rows):
    result = []
    for i in range(rows):
        start_char = ord('A') + i
        line = ""
        for j in range(rows, i, -1):
            line += chr(start_char + rows - j)
        result.append(line)
    return result

if __name__ == '__main__':
    sample_rows = 5
    pattern = create_inverted_alphabet_triangle(sample_rows)
    for line in pattern:
        print(line)