import math
def compare_distances(d1: float, d2: float) -> dict:
    diff = abs(d1 - d2)
    return {
        "distance_1": round(d1, 6),
        "distance_2": round(d2, 6),
        "absolute_difference": round(diff, 6),
        "comparison_result": "equal" if math.isclose(d1, d2) else f"{d1} is greater than {d2}"
    }
if __name__ == '__main__':
    result = compare_distances(3.141592653589793, 3.1415926535)
    print(result)