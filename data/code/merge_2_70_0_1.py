def compare_distances(d1: float, d2: float) -> tuple[float, float]:
    if d1 > d2:
        return (d1, d1 - d2)
    else:
        return (d2, d2 - d1)
if __name__ == '__main__':
    value_a = 45.6789
    value_b = 30.1234
    result_value, difference = compare_distances(value_a, value_b)
    print(f"Larger distance: {result_value}")
    print(f"Difference: {difference}")