def calculate_absolute_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weight_a = 60.0
    sample_weight_b = 55.8
    difference_value = calculate_absolute_difference(sample_weight_a, sample_weight_b)
    print(difference_value)