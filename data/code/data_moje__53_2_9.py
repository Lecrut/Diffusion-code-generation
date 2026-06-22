def reverse_number_triangle(height: int) -> list:
    result = []
    for i in range(height, 0, -1):
        row = ' '.join(str(j) for j in range(1, i + 1))
        result.append(row)
    return result

if __name__ == '__main__':
    sample_height = 6
    output_lines = reverse_number_triangle(sample_height)
    for line in output_lines:
        print(line)