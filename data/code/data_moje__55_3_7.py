def inverted_alphabet_triangle(rows):
    result = []
    for i in range(rows):
        chars = [chr(ord('A') + j) for j in range(rows - i)]
        spaces = ' ' * (i * 2)
        result.append(spaces + ' '.join(chars))
    return '\n'.join(result)

if __name__ == '__main__':
    sample_rows = 5
    output = inverted_alphabet_triangle(sample_rows)
    print(output)