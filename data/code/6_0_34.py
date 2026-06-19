def calculate_weight_difference(a, b):
    return abs(a - b)

if __name__ == '__main__':
    sample_value1 = 75.3
    sample_value2 = 68.9
    difference = calculate_weight_difference(sample_value1, sample_value2)
    print(difference)