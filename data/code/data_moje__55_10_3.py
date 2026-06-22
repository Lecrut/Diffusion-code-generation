def print_alphabet_triangle(height):
    result = []
    for i in range(1, height + 1):
        chars = []
        for j in range(i):
            chars.append(chr(ord('A') + j))
        row = ' '.join(chars)
        result.append(row)
    for line in result:
        print(line)
    return result

if __name__ == '__main__':
    height = 5
    print_alphabet_triangle(height)