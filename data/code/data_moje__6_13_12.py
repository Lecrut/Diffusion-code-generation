def compute_weight_difference(weight1: float, weight2: float) -> float:
    return weight1 - weight2

if __name__ == "__main__":
    w1 = 10.5
    w2 = 7.3
    result = compute_weight_difference(w1, w2)
    print(result)