if __name__ == '__main__':
    n_terms = 12
    triangular_numbers = [n * (n + 1) // 2 for n in range(1, n_terms + 1)]
    print(triangular_numbers)