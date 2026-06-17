import sys
def compare_distances(d1: float, d2: float) -> str:
    epsilon = 1e-9
    if abs(d1 - d2) < epsilon:
        return "Equal"
    elif d1 > d2 + epsilon:
        return f"d1 ({d1}) is greater than d2 ({d2})"
    else:
        return f"d2 ({d2}) is greater than d1 ({d1})"
if __name__ == '__main__':
    distance_a = 3.141592653589793
    distance_b = 3.141592653589793
    result = compare_distances(distance_a, distance_b)
    print(result)