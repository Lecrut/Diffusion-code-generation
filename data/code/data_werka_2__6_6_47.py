def calculate_weight_difference(weight1: float, weight2: float) -> float:
    return abs(weight1 - weight2)

if __name__ == '__main__':
    SAMPLE_WEIGHT_1 = 85.0
    SAMPLE_WEIGHT_2 = 79.2
    difference = calculate_weight_difference(SAMPLE_WEIGHT_1, SAMPLE_WEIGHT_2)
    print(difference)