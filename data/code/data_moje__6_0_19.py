def calculate_weight_difference(w1: float, w2: float) -> float:
    diff = w1 - w2
    if diff >= 0:
        return diff
    return -diff

if __name__ == '__main__':
    result = calculate_weight_difference(10.5, 3.2)
    print(result)