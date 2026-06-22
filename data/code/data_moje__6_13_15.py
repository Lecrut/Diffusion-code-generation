def weight_difference(weight1: float, weight2: float) -> float:
    return abs(weight1 - weight2)

if __name__ == '__main__':
    w1 = 85.5
    w2 = 72.3
    print(weight_difference(w1, w2))