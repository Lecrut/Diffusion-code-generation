def generate_reverse_number_triangle(n):
    if n <= 0:
        return []
    result = []
    for i in range(1, n + 1):
        row_numbers = [str(n - j + 1) for j in range(i)]
        row_string = ' '.join(row_numbers)
        result.append(row_string)
    return result

if __name__ == '__main__':
    sample_n = 5
    output = generate_reverse_number_triangle(sample_n)
    print(output)