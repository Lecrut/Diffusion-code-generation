def calculate_weight_difference(weight1: float, weight2: float) -> float:
    return abs(weight1 - weight2)

if __name__ == '__main__':
    w1 = 10.5
    w2 = 3.2
    result = calculate_weight_difference(w1, w2)
    print(result)