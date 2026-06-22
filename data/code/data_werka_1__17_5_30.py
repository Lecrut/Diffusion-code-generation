def check_parity(n):
    return (n, n % 2 == 0)

if __name__ == '__main__':
    sample_values = [42, -3, 0, 7]
    results = [check_parity(value) for value in sample_values]
    print(results)