def generate_right_aligned_alphabet_triangle(n_rows):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if n_rows > len(alphabet):
        n_rows = len(alphabet)
    lines = []
    for i in range(1, n_rows + 1):
        letters = alphabet[:i]
        padding = " " * (n_rows - i)
        lines.append(padding + letters)
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_right_aligned_alphabet_triangle(5)
    print(result)