def calculate_difference(weight1: float, weight2: float) -> float:
    return weight1 - weight2

if __name__ == '__main__':
    weight_a = 150.5
    weight_b = 120.3
    result = calculate_difference(weight_a, weight_b)
    print(result)