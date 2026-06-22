def calculate_weight_difference(weight_a, weight_b):
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    sample_weight_a = 150
    sample_weight_b = 120
    result = calculate_weight_difference(sample_weight_a, sample_weight_b)
    print(result)