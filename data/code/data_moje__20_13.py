def is_even_via_lookup(n: int) -> bool:
    sample_values = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    return n in sample_values

if __name__ == '__main__':
    test_values = [0, 1, 2, 3, 4, 5, 10, 11, 100, 101]
    for value in test_values:
        result = is_even_via_lookup(value)
        print(result)