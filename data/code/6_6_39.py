def calculate_weight_difference(weight1: float, weight2: float) -> float:
    return abs(weight1 - weight2)

if __name__ == '__main__':
    SAMPLE_WEIGHT_1 = 70.5
    SAMPLE_WEIGHT_2 = 65.8
    difference = calculate_weight_difference(SAMPLE_WEIGHT_1, SAMPLE_WEIGHT_2)
    print(difference)