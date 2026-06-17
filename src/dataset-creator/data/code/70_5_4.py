import sys
def compare_distances(m1: float, m2: float) -> str:
    epsilon = 1e-9
    if abs(m1 - m2) < epsilon:
        return "Equal"
    elif m1 > m2 + epsilon:
        return f"{m1} is greater than {m2}"
    else:
        return f"{m2} is greater than {m1}"
if __name__ == '__main__':
    distance_a = 45.6789012345
    distance_b = 45.6789012345
    result = compare_distances(distance_a, distance_b)
    print(result)