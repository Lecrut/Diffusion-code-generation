def generate_number_pyramid():
    rows = 3
    lines = []
    for i in range(1, rows + 1):
        line = ' '.join(str(j) for j in range(1, i + 1))
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_number_pyramid()
    print(result)