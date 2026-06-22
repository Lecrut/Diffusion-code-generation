def generate_right_aligned_pyzramid(rows):
    result = []
    for i in range(1, rows + 1):
        numbers = list(range(1, i + 1))
        line = ' '.join(map(str, numbers))
        result.append(line)
    max_width = len(' '.join(map(str, range(1, rows + 1))))
    pyramided_lines = []
    for line in result:
        padding = (max_width - len(line)) // 2
        pyramided_lines.append(' ' * padding + line)
    return pyramided_lines

if __name__ == '__main__':
    rows = 5
    output = generate_right_aligned_pyzramid(rows)
    for line in output:
        print(line)