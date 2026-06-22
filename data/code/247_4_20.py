def sum_large_integers(a, b):
    return a + b

if __name__ == '__main__':
    large_a = 123456789012345678901234567890
    large_b = 987654321098765432109876543210
    result = sum_large_integers(large_a, large_b)
    print(result)