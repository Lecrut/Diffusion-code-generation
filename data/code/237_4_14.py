def calculate_triangular_numbers():
    return [n * (n + 1) // 2 for n in range(1, 13)]

if __name__ == '__main__':
    sample_count = 6
    triangular_result = calculate_triangular_numbers()[:sample_count]
    print(triangular_result)