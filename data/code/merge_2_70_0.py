def compare_distances(val1: float, val2: float) -> tuple[float, float]:
    if val1 > val2:
        return (val1, val1 - val2)
    else:
        return (val2, abs(val1 - val2))
if __name__ == '__main__':
    distance_a = 50.7
    distance_b = 43.2
    larger_value, difference = compare_distances(distance_a, distance_b)
    print(f"Larger value: {larger_value}")
    print(f"Difference: {difference}")