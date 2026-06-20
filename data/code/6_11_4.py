import math

def calculate_absolute_difference(weight_a: float, weight_b: float) -> float:
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    w1 = 10.5
    w2 = 3.2
    result = calculate_absolute_difference(w1, w2)
    print(result)