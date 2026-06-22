def triangular_numbers():
    return [n * (n + 1) // 2 for n in range(1, 13)]

if __name__ == '__main__':
    sample_triangulars = triangular_numbers()
    print(sample_triangulars)