def inverted_alphabet_triangle(size=5):
    result = []
    for i in range(size):
        row = ""
        for j in range(size):
            if i >= j:
                char = chr(ord('A') + (i - j))
                row += char + " "
        result.append(row.strip())
    return result

if __name__ == '__main__':
    pattern = inverted_alphabet_triangle(5)
    for line in pattern:
        print(line)