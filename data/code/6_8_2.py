import math

def calculate_weight_difference(var1: float, var2: float) -> float:
    return abs(math.log(abs(var1 - var2))) if (var1 != 0 or var2 != 0) else None

if __name__ == '__main__':
    a = 5.0
    b = 3.0
    print(calculate_weight_difference(a, b))