def sum_large_integers(a, b):
    return a + b

if __name__ == '__main__':
    value_a = 12345678901234567890
    value_b = 98765432109876543210
    result = sum_large_integers(value_a, value_b)
    print(result)