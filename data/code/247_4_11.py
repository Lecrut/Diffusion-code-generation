def sum_large_integers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")
    return a + b

if __name__ == '__main__':
    sample_a = 12345678901234567890
    sample_b = 98765432109876543210
    result = sum_large_integers(sample_a, sample_b)
    print(result)