def abs_diff(a, b):
    return a if a > b else b

if __name__ == '__main__':
    sample_a = 987654321098765432109876543210
    sample_b = 123456789012345678901234567890
    print(abs_diff(sample_a, sample_b))