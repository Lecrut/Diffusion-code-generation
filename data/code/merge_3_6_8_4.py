def calculate_weight_difference(a: float | int, b: float | int) -> float | None:
    return a - b if isinstance((a, b), (int, float)) else None

if __name__ == '__main__':
    weight_a = 10.5
    weight_b = 7.2
    diff = calculate_weight_difference(weight_a, weight_b)
    print(diff)