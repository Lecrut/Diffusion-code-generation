def calculate_weight_difference(a, b):
    return abs(a - b)

if __name__ == '__main__':
    sample_value1 = 5.75
    sample_value2 = 3.25
    difference = calculate_weight_difference(sample_value1, sample_value2)
    print(difference)