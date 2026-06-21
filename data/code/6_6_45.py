def calculate_weight_difference(weight1: float, weight2: float) -> float:
    difference = weight1 - weight2
    return abs(difference)

if __name__ == '__main__':
    sample_weight_a = 60.3
    sample_weight_b = 58.9
    result = calculate_weight_difference(sample_weight_a, sample_weight_b)
    print(result)