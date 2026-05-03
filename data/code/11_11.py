import math
def calculate_length_ratio(length1: float, length2: float) -> float:
    if length2 == 0.0:
        return float('inf') if length1 != 0.0 else float('nan')
    return length1 / length2
if __name__ == '__main__':
    a = 10.0
    b = 3.0
    result1 = calculate_length_ratio(a, b)
    print(result1)
    c = 0.0
    d = 5.0
    result2 = calculate_length_ratio(a, c)
    print(result2)
    e = 0.0
    f = 0.0
    result3 = calculate_length_ratio(e, f)
    print(result3)
    g = -4.5
    h = 2.0
    result4 = calculate_length_ratio(g, h)
    print(result4)