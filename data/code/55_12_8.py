def generate_alphabet_triangle(n):
    alphabet = [chr(i) for i in range(ord('A'), ord('A') + 26)]
    result = []
    for i in range(1, n + 1):
        row = ' '.join(alphabet[:i])
        result.append(row)
    return '\n'.join(result)

if __name__ == '__main__':
    sample_size = 5
    print(generate_alphabet_triangle(sample_size))