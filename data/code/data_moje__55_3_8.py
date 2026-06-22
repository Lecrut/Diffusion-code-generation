def inverted_alphabet_triangle(n):
    if n < 0:
        return []
    result = []
    for i in range(n):
        row = []
        for j in range(n - i):
            char_code = ord('Z') - j
            row.append(chr(char_code))
        result.append(' '.join(row))
    return result

if __name__ == '__main__':
    sample_n = 5
    print(inverted_alphabet_triangle(sample_n))