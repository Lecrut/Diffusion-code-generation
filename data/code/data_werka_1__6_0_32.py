def calculate_weight_difference(a, b):
    return abs(a - b)

if __name__ == '__main__':
    sample_value1 = 45.789
    sample_value2 = 32.456
    result = calculate_weight_difference(sample_value1, sample_value2)
    print(result)