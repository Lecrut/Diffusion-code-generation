def print_centered_alphabet_triangle(height):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(1, height + 1):
        chars = alphabet[:i]
        if i == 1:
            line = chars
        else:
            line = chars + chars[-2::-1]
        padding = height - i
        print(" " * padding + line + " " * padding)

if __name__ == '__main__':
    sample_height = 5
    print_centered_alphabet_triangle(sample_height)