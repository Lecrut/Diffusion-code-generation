def inverted_alphabet_triangle(rows):
    if rows <= 0:
        return ""
    result = []
    alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    for i in range(rows):
        if i >= len(alphabet):
            break
        line = ' '.join(alphabet[len(alphabet) - 1 - i::-1])
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    sample_rows = 5
    print(inverted_alphabet_triangle(sample_rows))