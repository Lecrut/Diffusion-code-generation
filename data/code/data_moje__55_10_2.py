def alphabet_triangle(height):
    lines = []
    for i in range(1, height + 1):
        letters = [chr(ord('A') + j) for j in range(i)]
        line = ''.join(letters)
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = alphabet_triangle(5)
    print(result)