def generate_pyramid(rows):
    lines = []
    for i in range(1, rows + 1):
        line = (str(i) + ' ') * i
        lines.append(line.rstrip())
    return lines

if __name__ == '__main__':
    pyramid_lines = generate_pyramid(5)
    for line in pyramid_lines:
        print(line)