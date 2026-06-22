def generate_pyramid(rows):
    result = []
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        result.append(spaces + numbers)
    return result

if __name__ == '__main__':
    sample_rows = 5
    output = generate_pyramid(sample_rows)
    for line in output:
        print(line)