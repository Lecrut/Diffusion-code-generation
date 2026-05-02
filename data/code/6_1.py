def calculate_weight_difference(a: float, b: float) -> float:
    return abs(a - b)
if __name__ == '__main__':
    weight1 = 10.5
    weight2 = 5.2
    difference = calculate_weight_difference(weight1, weight2)
    print(difference)