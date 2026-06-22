def generate_alphabet_triangle(size: int) -> list:
    import string
    alphabet = string.ascii_uppercase
    result = []
    for i in range(1, size + 1):
        chars = alphabet[:i]
        line = ''.join(chars)
        result.append(line)
    return result

if __name__ == '__main__':
    sample_size = 5
    triangle = generate_alphabet_triangle(sample_size)
    for line in triangle:
        print(line)