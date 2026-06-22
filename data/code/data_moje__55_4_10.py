def generate_alphabet_pyramid(rows):
    alphabet = [chr(code) for code in range(ord('A'), ord('Z') + 1)]
    pyramid = []
    for i in range(rows):
        current_row = [alphabet[j % len(alphabet)] for j in range(i + 1)]
        pyramid.append(" ".join(current_row))
    return pyramid

if __name__ == '__main__':
    sample_rows = 5
    result = generate_alphabet_pyramid(sample_rows)
    for line in result:
        print(line)