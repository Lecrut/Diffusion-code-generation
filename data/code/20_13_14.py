def is_even_by_lookup(number):
    sample_values = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    if number in sample_values:
        return True
    return False

if __name__ == '__main__':
    test_values = [0, 1, 2, 3, 10, 11, 100]
    for value in test_values:
        result = is_even_by_lookup(value)
        print(f"{value}: {result}")