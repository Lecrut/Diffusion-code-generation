def calculate_weight_difference(weight1: float, weight2: float) -> float:
    diff = weight1 - weight2
    if diff < 0:
        return -diff
    return diff

if __name__ == '__main__':
    result = calculate_weight_difference(150.5, 145.2)
    print(result)