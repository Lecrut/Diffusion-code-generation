def is_even_by_lookup(n: int) -> bool:
    sample_values = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    return n in sample_values

if __name__ == '__main__':
    test_values = [2, 5, 10, 11, 0, 7]
    results = []
    for val in test_values:
        results.append(is_even_by_lookup(val))
    for val, res in zip(test_values, results):
        print(f"{val}: {res}")