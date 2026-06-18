def compare_distances(distance_a: int | float, distance_b: int | float) -> str:
    val_a = float(distance_a)
    val_b = float(distance_b)
    if val_a < val_b:
        return f"{distance_a} is smaller than {distance_b}"
    elif val_a > val_b:
        return f"{distance_a} is larger than {distance_b}"
    else:
        return f"{distance_a} equals {distance_b}"
if __name__ == '__main__':
    d1 = 9007199254740993                                                              
    d2 = 8_000_000_000_000_000
    result = compare_distances(d1, d2)
    print(result)