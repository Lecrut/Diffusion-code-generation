def generate_pyramid(rows):
    lines = []
    for i in range(1, rows + 1):
        line = str(i) * i
        lines.append(line.rjust(rows * 2))
    return lines

if __name__ == '__main__':
    result = generate_pyramid(5)
    for line in result:
        print(line)