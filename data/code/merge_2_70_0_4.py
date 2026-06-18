def compare_distances(d1: float, d2: float) -> tuple[float, float]:
    if d1 > d2:
        return (d1, d1 - d2)
    else:
        return (d2, abs(d2 - d1))
if __name__ == '__main__':
    val_a = 45.7
    val_b = 30.2
    result_val, diff = compare_distances(val_a, val_b)
    print(f"Larger value: {result_val}, Difference: {diff}")