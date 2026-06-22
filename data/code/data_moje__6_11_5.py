def calculate_absolute_weight_difference(weight1: float, weight2: float) -> float:
    return abs(weight1 - weight2)

if __name__ == '__main__':
    weight_a = 75.5
    weight_b = 82.3
    result = calculate_absolute_weight_difference(weight_a, weight_b)
    print(result)