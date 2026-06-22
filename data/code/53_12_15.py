def generate_reverse_number_triangle(size):
    lines = []
    for i in range(size, 0, -1):
        row_numbers = list(range(1, i + 1))
        row_str = ' '.join(map(str, row_numbers))
        lines.append(row_str)
    return '\n'.join(lines)

if __name__ == '__main__':
    sample_size = 5
    result = generate_reverse_number_triangle(sample_size)
    print(result)