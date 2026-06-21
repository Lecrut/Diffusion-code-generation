def is_divisible_by_two(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [10, 15, 20, 23, 100, 99]
    results = []
    for value in test_values:
        result = is_divisible_by_two(value)
        results.append(result)
    for value, result in zip(test_values, results):
        print(value, result)