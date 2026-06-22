def generate_number_pyramid(height=5):
    lines = []
    for i in range(1, height + 1):
        numbers = []
        for j in range(1, i + 1):
            numbers.append(str(j))
        for j in range(i - 1, 0, -1):
            numbers.append(str(j))
        line = ' '.join(numbers)
        max_width = len(' '.join([str(i) for i in range(1, i + 1)] + [str(i) for i in range(i - 1, 0, -1)]))
        line = line.center(max_width * (height - i + 1) + (height - i) * 2)
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    result = generate_number_pyramid(5)
    print(result)