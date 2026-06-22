def calculate_weight_difference(weight1: float, weight2: float) -> float:
    return abs(weight1 - weight2)

if __name__ == '__main__':
    result = calculate_weight_difference(150.5, 140.2)
    print(result)