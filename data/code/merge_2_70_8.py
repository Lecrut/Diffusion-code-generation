import math
def compare_distances(d1: float, d2: float) -> dict:
    diff = abs(d1 - d2)
    return {
        "distance_1": d1,
        "distance_2": d2,
        "absolute_difference": round(diff, 6),
        "comparison_result": "equal" if math.isclose(d1, d2) else ("d1_greater" if d1 > d2 else "d2_greater")
    }
if __name__ == '__main__':
    result = compare_distances(5.0, 3.141592653589793)
    print(result)