def generate_hollow_pyramid(rows):
    result = []
    for i in range(rows):
        line = []
        for j in range(rows - i - 1):
            line.append(' ')
        for k in range(2 * i + 1):
            if k == 0 or k == 2 * i or i == rows - 1:
                line.append('*')
            else:
                line.append(' ')
        result.append(''.join(line))
    return result

if __name__ == '__main__':
    sample_rows = 5
    pattern = generate_hollow_pyramid(sample_rows)
    for line in pattern:
        print(line)