def triangular_numbers(n=12):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    return [n * (n + 1) // 2 for n in range(1, n + 1)]

if __name__ == '__main__':
    triangular_result = triangular_numbers()
    print(triangular_result)