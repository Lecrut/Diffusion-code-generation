def generate_alphabet_triangle():
    result = []
    for i in range(1, 27):
        row = ""
        for j in range(1, i + 1):
            row += chr(ord('A') + j - 1)
        result.append(row)
    return result

if __name__ == '__main__':
    triangle = generate_alphabet_triangle()
    for line in triangle:
        print(line)