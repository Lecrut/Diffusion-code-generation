def calculate_weight_difference(weight1: float, weight2: float) -> float:
    return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weight1 = 85.0
    sample_weight2 = 92.3
    difference = calculate_weight_difference(sample_weight1, sample_weight2)
    print(difference)