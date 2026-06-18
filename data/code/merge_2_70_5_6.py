import math
def compare_distances(m1: float, m2: float) -> str:
    epsilon = 1e-9
    if abs(m1 - m2) < epsilon:
        return "Equal"
    elif m1 > m2:
        return f"{m1} is greater than {m2}"
    else:
        return f"{m2} is greater than {m1}"
if __name__ == '__main__':
    distance_a = 3.14159265358979
    distance_b = 3.14159265358979 + 0.0000000001
    result = compare_distances(distance_a, distance_b)
    print(result)