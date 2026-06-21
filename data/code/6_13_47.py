def calculate_absolute_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weight_1 = 70.25
    sample_weight_2 = 65.40
    result = calculate_absolute_difference(sample_weight_1, sample_weight_2)
    print(result)