import math
def compare_distances(d1: float, d2: float) -> dict:
    diff = abs(d1 - d2)
    return {
        "distance_1": round(d1, 6),
        "distance_2": round(d2, 6),
        "difference": round(diff, 6),
        "comparison_result": f"{d1} is {'greater than' if d1 > d2 else 'less than or equal to'} {d2}"
    }
if __name__ == '__main__':
    result = compare_distances(5.073498, 6.2)
    print(result)