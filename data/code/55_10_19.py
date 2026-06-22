def print_alphabet_triangle(height):
    if height <= 0:
        return
    alphabet = [chr(code) for code in range(ord('A'), ord('Z') + 1)]
    for i in range(1, height + 1):
        line = []
        for j in range(i):
            line.append(alphabet[j % 26])
        print(' '.join(line))

if __name__ == '__main__':
    sample_height = 5
    print_alphabet_triangle(sample_height)