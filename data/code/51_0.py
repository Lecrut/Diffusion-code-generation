def generate_pyramid(rows):
    lines = []
    for i in range(1, rows + 1):
        line = ' ' * (rows - i) + str(i) * i
        lines.append(line)
    return lines

if __name__ == '__main__':
    pyramid = generate_pyramid(5)
    for line in pyramid:
        print(line)