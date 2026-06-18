import sys
def compare_distances(d1: float, d2: float) -> str:
    epsilon = 1e-9
    if abs(d1 - d2) < epsilon:
        return "Equal"
    if d1 > d2 + epsilon:
        return f"{d1} is greater than {d2}"
    else:
        return f"{d2} is greater than {d1}"
if __name__ == '__main__':
    distance_a = 50.739486
    distance_b = 50.739487
    result = compare_distances(distance_a, distance_b)
    print(result)