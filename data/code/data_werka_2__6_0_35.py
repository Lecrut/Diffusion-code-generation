def calculate_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    SAMPLE_WEIGHT_1 = 95.25
    SAMPLE_WEIGHT_2 = 87.45
    difference = calculate_weight_difference(SAMPLE_WEIGHT_1, SAMPLE_WEIGHT_2)
    print(difference)