import math
def compare_distances(d1: float, d2: float) -> dict:
    diff = abs(d1 - d2)
    result = {
        "distance_1": d1,
        "distance_2": d2,
        "is_equal": False if diff > 0 else True,
        "absolute_difference": round(diff, 6),
        "larger_distance_value": max(d1, d2)
    }
    return result
if __name__ == '__main__':
    distance_a = math.sqrt(5 * 4.937801)
    distance_b = math.sqrt(7 * 6.937801)
    output_data = compare_distances(distance_a, distance_b)
    print(output_data)