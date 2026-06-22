def generate_alphabet_pyramid(rows):
    result = []
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(1, rows + 1):
        letters = alphabet[:i]
        line = ' '.join(letters)
        result.append(line)
    return result

if __name__ == '__main__':
    sample_rows = 5
    pyramid_lines = generate_alphabet_pyramid(sample_rows)
    for line in pyramid_lines:
        print(line)