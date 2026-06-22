def generate_pyramid():
    lines = []
    for i in range(1, 6):
        line = '0' * (2 * i - 1)
        lines.append(line)
    return lines

if __name__ == '__main__':
    result = generate_pyramid()
    for line in result:
        print(line)