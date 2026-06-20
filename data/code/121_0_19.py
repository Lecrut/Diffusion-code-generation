def compare_values(value1, value2):
    return max(value1, value2)

if __name__ == '__main__':
    sample_value1 = 12345678901234567890
    sample_value2 = 98765432109876543210
    larger_value = compare_values(sample_value1, sample_value2)
    print(f"Value 1: {sample_value1}")
    print(f"Value 2: {sample_value2}")
    print(f"Larger Value: {larger_value}")