def print_centered_alphabet_triangle(height):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(height):
        if i >= len(alphabet):
            char = alphabet[i % len(alphabet)]
            row = char * (2 * i + 1)
        else:
            char = alphabet[i]
            row = char * (2 * i + 1)
        print(row.center(2 * height + (height - 1)))

if __name__ == '__main__':
    sample_height = 5
    print_centered_alphabet_triangle(sample_height)