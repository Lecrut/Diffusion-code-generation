def generate_alphabet_triangle(size: int) -> list[str]:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i in range(1, size + 1):
        row_chars = [alphabet[j % 26] for j in range(i)]
        row_str = " ".join(row_chars)
        result.append(row_str)
    return result

if __name__ == '__main__':
    sample_size = 5
    triangle = generate_alphabet_triangle(sample_size)
    for line in triangle:
        print(line)