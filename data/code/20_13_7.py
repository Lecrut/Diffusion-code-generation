def is_even_by_lookup(n: int) -> bool:
    sample_values = {0, 2, 4, 6, 8, 10, -2, -4, -6}
    if n in sample_values:
        return True
    return (n % 2) == 0

if __name__ == '__main__':
    test_values = [4, 7, -2, 15, 0, 33, 100]
    for value in test_values:
        result = is_even_by_lookup(value)
        print(f"{value}: {result}")