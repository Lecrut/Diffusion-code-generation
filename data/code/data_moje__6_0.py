def calculate_weight_difference(a: float, b: float) -> float:
    diff = a - b
    if diff < 0:
        return -diff
    return diff

if __name__ == '__main__':
    weight1 = 150.5
    weight2 = 148.2
    result = calculate_weight_difference(weight1, weight2)
    print(result)