def generate_alphabet_triangle(size: int) -> list[str]:
    import string
    alphabet = string.ascii_uppercase
    triangle = []
    current_chars = []
    for i in range(size):
        current_chars.append(alphabet[i % 26])
        triangle.append(" ".join(current_chars))
    return triangle

if __name__ == '__main__':
    sample_size = 5
    result = generate_alphabet_triangle(sample_size)
    for line in result:
        print(line)