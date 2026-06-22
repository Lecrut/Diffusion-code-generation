def print_inverted_alphabet_triangle(n):
    result = []
    for i in range(n):
        row = []
        for j in range(n - i):
            row.append(chr(65 + (i + j) % 26))
        result.append(" ".join(row))
    return "\n".join(result)

if __name__ == '__main__':
    sample_n = 5
    output = print_inverted_alphabet_triangle(sample_n)
    print(output)