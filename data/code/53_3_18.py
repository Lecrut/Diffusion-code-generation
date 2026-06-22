def generate_left_aligned_reverse_triangle(num_rows=5):
    result = []
    for i in range(num_rows, 0, -1):
        row_numbers = list(range(1, i + 1))
        row_strings = [str(n) for n in row_numbers]
        row_line = ''.join(row_strings)
        result.append(row_line)
    return result

if __name__ == '__main__':
    output = generate_left_aligned_reverse_triangle(5)
    for line in output:
        print(line)