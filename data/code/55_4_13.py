def print_pyramid_alphabet(rows):
    alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    for i in range(1, rows + 1):
        chars = [alphabet[j] for j in range(i)]
        line = " ".join(chars)
        print(" " * (rows - i) + line + " " * (rows - i))

if __name__ == '__main__':
    print_pyramid_alphabet(5)