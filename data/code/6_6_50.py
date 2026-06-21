def calculate_weight_difference(weight1: float, weight2: float) -> float:
    return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weight1 = 78.9
    sample_weight2 = 64.1
    difference = calculate_weight_difference(sample_weight1, sample_weight2)
    print(difference)