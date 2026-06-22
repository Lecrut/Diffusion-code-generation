def generate_reverse_number_triangle(rows):
    lines = []
    for i in range(rows, 0, -1):
        line = ' '.join(str(i) for _ in range(i))
        lines.append(line)
    return lines

if __name__ == '__main__':
    result = generate_reverse_number_triangle(6)
    for line in result:
        print(line)