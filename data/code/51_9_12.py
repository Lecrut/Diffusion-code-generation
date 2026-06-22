def build_pyramid():
    rows = 6
    lines = []
    for i in range(1, rows + 1):
        number = i
        line_numbers = []
        for j in range(1, i + 1):
            line_numbers.append(str(number))
        for j in range(i - 2, 0, -1):
            line_numbers.append(str(j))
        combined = " ".join(line_numbers)
        padding = " " * (rows - i)
        line = padding + combined
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    print(build_pyramid())