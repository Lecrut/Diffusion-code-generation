def calculate_absolute_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    SAMPLE_WEIGHT_1 = 82.45
    SAMPLE_WEIGHT_2 = 78.90
    difference = calculate_absolute_difference(SAMPLE_WEIGHT_1, SAMPLE_WEIGHT_2)
    print(difference)