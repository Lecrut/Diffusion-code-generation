def print_centered_alphabet_triangle(height):
    if height < 1:
        return
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if height > len(alphabet):
        height = len(alphabet)
    for i in range(1, height + 1):
        line_chars = []
        for j in range(i):
            line_chars.append(alphabet[j])
        for j in range(i - 2, -1, -1):
            line_chars.append(alphabet[j])
        line = "".join(line_chars)
        total_width = 2 * height - 1
        padding = (total_width - len(line)) // 2
        print(" " * padding + line)

if __name__ == '__main__':
    sample_height = 5
    print_centered_alphabet_triangle(sample_height)