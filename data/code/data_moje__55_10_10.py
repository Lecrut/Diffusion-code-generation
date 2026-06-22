def alphabet_triangle(height):
    lines = []
    for i in range(1, height + 1):
        line = ""
        for j in range(i):
            char_code = ord('A') + j
            line += chr(char_code)
        lines.append(line)
    return lines

if __name__ == '__main__':
    result = alphabet_triangle(5)
    for line in result:
        print(line)