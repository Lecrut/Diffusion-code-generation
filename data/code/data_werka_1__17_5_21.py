def get_number_and_parity(n):
    return (n, n % 2 == 0)

if __name__ == '__main__':
    sample_values = [0, 1, 2, -3, 42, -57]
    results = [get_number_and_parity(value) for value in sample_values]
    for result in results:
        print(result)