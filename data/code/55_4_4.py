def generate_alphabet_pyramid(rows):
    result = []
    for i in range(1, rows + 1):
        chars = [chr(65 + j) for j in range(i)]
        result.append(" ".join(chars))
    return "\n".join(result)

if __name__ == '__main__':
    sample_rows = 5
    print(generate_alphabet_pyramid(sample_rows))