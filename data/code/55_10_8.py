def print_alphabet_triangle(height):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for row in range(1, height + 1):
        if row > len(alphabet):
            break
        pattern = ''
        for col in range(1, row + 1):
            pattern += alphabet[col - 1]
        print(pattern)

if __name__ == '__main__':
    sample_height = 5
    print_alphabet_triangle(sample_height)