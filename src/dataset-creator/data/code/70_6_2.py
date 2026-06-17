def compare_distances(d1: float, d2: float) -> tuple[float, float]:
    if d1 >= d2:
        return d1, d1 - d2
    else:
        return d2, d2 - d1
if __name__ == '__main__':
    result = compare_distances(5.0, 3.7)
    print(f"Larger distance: {result[0]}, Difference: {result[1]}")