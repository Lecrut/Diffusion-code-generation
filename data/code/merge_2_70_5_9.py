import sys
def compare_distances(d1: float, d2: float) -> str:
    if abs(d1 - d2) < 1e-9:
        return "Equal"
    elif d1 > d2 + 1e-9:
        return f"{d1} is greater than {d2}"
    else:
        return f"{d2} is greater than {d1}"
if __name__ == '__main__':
    distance_a = 45.6789012345
    distance_b = 45.6789012345
    result = compare_distances(distance_a, distance_b)
    print(result)