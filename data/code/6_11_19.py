def calculate_absolute_difference(weight1: float, weight2: float) -> float:
    return abs(weight1 - weight2)

if __name__ == '__main__':
    w1: float = 10.5
    w2: float = 3.2
    result: float = calculate_absolute_difference(w1, w2)
    print(result)