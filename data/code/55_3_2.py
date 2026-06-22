def generate_inverted_alphabet_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        row_chars = [chr(65 + j) for j in range(i)]
        result.append(" ".join(row_chars))
    return result

if __name__ == '__main__':
    sample_rows = 5
    print(generate_inverted_alphabet_triangle(sample_rows))