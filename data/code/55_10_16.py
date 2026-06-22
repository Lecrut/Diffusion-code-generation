def print_alphabet_triangle(height):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lines = []
    for i in range(1, height + 1):
        current_line = ""
        for j in range(i):
            current_line += alphabet[j % 26]
        lines.append(current_line)
    return "\n".join(lines)

if __name__ == '__main__':
    hard_coded_height = 5
    result = print_alphabet_triangle(hard_coded_height)
    print(result)