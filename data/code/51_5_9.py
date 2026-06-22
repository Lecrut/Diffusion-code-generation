def generate_hollow_pyramid(rows):
    if rows <= 0:
        return []
    result = []
    for i in range(1, rows + 1):
        line = ""
        for j in range(1, rows + 1):
            if j <= rows - i:
                line += "  "
            elif j == rows - i + 1 or j == rows - i + (2 * i - 2) or i == 1 or i == rows:
                line += str(i) + " "
            else:
                line += "  "
        result.append(line.rstrip())
    return result

if __name__ == '__main__':
    rows = 5
    pyramid_lines = generate_hollow_pyramid(rows)
    for line in pyramid_lines:
        print(line)