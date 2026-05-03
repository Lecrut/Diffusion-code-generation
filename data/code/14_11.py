def compare_volumes(vol1: float, vol2: float) -> tuple[float, float, float]:
    if vol1 >= vol2:
        larger = vol1
        smaller = vol2
    else:
        larger = vol2
        smaller = vol1
    difference = abs(vol1 - vol2)
    return larger, smaller, difference
if __name__ == '__main__':
    a = 15.75
    b = 22.31
    larger, smaller, diff = compare_volumes(a, b)
    print(f"Larger: {larger}")
    print(f"Smaller: {smaller}")
    print(f"Difference: {diff}")
    c = 100.0
    d = 99.99
    larger_2, smaller_2, diff_2 = compare_volumes(c, d)
    print(f"Larger: {larger_2}")
    print(f"Smaller: {smaller_2}")
    print(f"Difference: {diff_2}")