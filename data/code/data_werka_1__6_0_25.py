def calculate_weight_difference(num1, num2):
    return abs(num1 - num2)

if __name__ == '__main__':
    sample_value1 = 45.6789
    sample_value2 = 34.5678
    difference = calculate_weight_difference(sample_value1, sample_value2)
    print(difference)