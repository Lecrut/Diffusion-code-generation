def print_alphabet_triangle(height):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lines = []
    for i in range(height):
        if i >= len(alphabet):
            break
        current_chars = alphabet[:i + 1]
        reversed_chars = current_chars[::-1]
        row = current_chars + reversed_chars[1:]
        lines.append(row)
    max_width = len(lines[-1]) if lines else 0
    for line in lines:
        print(line.center(max_width))

if __name__ == '__main__':
    print_alphabet_triangle(5)