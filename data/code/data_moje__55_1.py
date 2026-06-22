def print_centered_alphabet_triangle(height):
    if height <= 0:
        return
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(height):
        char = alphabet[i % len(alphabet)]
        spaces = " " * (height - i - 1)
        line = spaces + char + spaces
        print(line)

if __name__ == '__main__':
    print_centered_alphabet_triangle(5)