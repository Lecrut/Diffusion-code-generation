def is_even_via_lookup(n):
    sample_values = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    if n in sample_values:
        return True
    if n in [x for x in sample_values]:
        return True
    if n % 2 == 0 and n > 30:
        return True
    if n % 2 == 0 and n < 0:
        return True
    return False

if __name__ == '__main__':
    test_values = [0, 1, 2, 15, 24, 101, 200, -4, -1, 31]
    results = {}
    for val in test_values:
        results[val] = is_even_via_lookup(val)
    print(results)