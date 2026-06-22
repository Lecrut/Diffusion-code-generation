def compute_weight_difference(w1: float, w2: float) -> float:
    return w1 - w2

if __name__ == '__main__':
    weight1 = 10.5
    weight2 = 7.2
    result = compute_weight_difference(weight1, weight2)
    print(result)