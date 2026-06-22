def generate_reverse_number_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        line = ' '.join(str(num) for num in range(1, i + 1))
        result.append(line)
    return result

if __name__ == '__main__':
    sample_rows = 5
    pattern = generate_reverse_number_triangle(sample_rows)
    for line in pattern:
        print(line)