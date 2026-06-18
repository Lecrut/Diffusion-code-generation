import math
def compare_distances(d1: float, d2: float) -> dict:
    diff = abs(d1 - d2)
    return {
        "distance_1": d1,
        "distance_2": d2,
        "absolute_difference": round(diff, 6),
        "comparison_result": "equal" if math.isclose(d1, d2) else ("greater_than" if d1 > d2 else "less_than")
    }
if __name__ == '__main__':
    result = compare_distances(5.0, 3.789456)
    print(result)