def generate_triangle():
    rows = 5
    result = []
    for i in range(1, rows + 1):
        line = []
        for j in range(i):
            line.append(chr(65 + j))
        result.append("".join(line))
    return "\n".join(result)

if __name__ == '__main__':
    print(generate_triangle())