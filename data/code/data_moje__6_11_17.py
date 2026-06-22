def calculate_absolute_difference(weight_one, weight_two):
    return abs(weight_one - weight_two)

if __name__ == '__main__':
    sample_weight_a = 150.75
    sample_weight_b = 124.30
    result = calculate_absolute_difference(sample_weight_a, sample_weight_b)
    print(result)