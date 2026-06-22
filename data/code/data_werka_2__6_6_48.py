def calculate_weight_difference(weight1: float, weight2: float) -> float:
    return abs(weight1 - weight2)

if __name__ == '__main__':
    SAMPLE_WEIGHT1 = 95.3
    SAMPLE_WEIGHT2 = 88.7
    difference = calculate_weight_difference(SAMPLE_WEIGHT1, SAMPLE_WEIGHT2)
    print(difference)