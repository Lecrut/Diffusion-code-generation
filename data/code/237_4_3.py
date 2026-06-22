def generate_triangular_numbers(count):
    return [n * (n + 1) // 2 for n in range(1, count + 1)]

if __name__ == '__main__':
    sample_count = 6
    triangular_result = generate_triangular_numbers(sample_count)
    print(triangular_result)