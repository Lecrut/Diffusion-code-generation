def calculate_absolute_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    SAMPLE_WEIGHT_A = 80.0
    SAMPLE_WEIGHT_B = 75.0
    difference = calculate_absolute_difference(SAMPLE_WEIGHT_A, SAMPLE_WEIGHT_B)
    print(difference)