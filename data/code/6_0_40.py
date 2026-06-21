def calculate_weight_difference(weight1, weight2):
    difference = abs(weight1 - weight2)
    return difference

if __name__ == '__main__':
    sample_weight_a = 95.43
    sample_weight_b = 87.65
    result = calculate_weight_difference(sample_weight_a, sample_weight_b)
    print(result)