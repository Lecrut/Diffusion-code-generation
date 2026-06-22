def calculate_weight_difference(a: float, b: float) -> float:
    return abs(a - b)

if __name__ == '__main__':
    val1 = 10.5
    val2 = 7.2
    print(calculate_weight_difference(val1, val2))