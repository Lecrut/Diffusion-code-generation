def generate_zigzag_triangle(rows):
    result = []
    for i in range(rows):
        line = ""
        indent = rows - 1 - i
        line += " " * indent
        if i % 2 == 0:
            for j in range(i + 1):
                line += chr(ord('A') + j)
        else:
            chars = []
            for j in range(i + 1):
                chars.append(chr(ord('A') + j))
            line += "".join(reversed(chars))
        result.append(line)
    return result

if __name__ == '__main__':
    sample_rows = 7
    output = generate_zigzag_triangle(sample_rows)
    for line in output:
        print(line)