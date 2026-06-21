def is_even(n):
    bit_mask = 1
    is_zero_bit = (n & bit_mask) == 0
    return is_zero_bit

if __name__ == '__main__':
    test_values = [1024, 2049, -12, -13, 0, 1]
    for value in test_values:
        result = is_even(value)
        print(f"{value}: {result}")