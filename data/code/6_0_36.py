def calculate_weight_difference(weight1, weight2):
    difference = weight1 - weight2
    return abs(difference)

if __name__ == '__main__':
    sample_weight_a = 95.2
    sample_weight_b = 80.7
    result = calculate_weight_difference(sample_weight_a, sample_weight_b)
    print(result)