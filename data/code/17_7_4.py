def get_number_and_parity(n: int) -> tuple[int, bool]:
    return (n, n % 2 == 0)
if __name__ == '__main__':
    test_numbers = [1, 2, 3, 4, 5, 0, -2, -3]
    results = []
    for num in test_numbers:
        results.append(get_number_and_parity(num))
    print(results)