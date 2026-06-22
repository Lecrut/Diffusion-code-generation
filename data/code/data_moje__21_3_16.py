import math

def find_largest(a: float, b: float, c: float) -> float:
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

if __name__ == '__main__':
    x, y, z = 3.14, 1.41, 2.72
    result = find_largest(x, y, z)
    print(result)