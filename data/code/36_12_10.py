import math

def trapezoid_area(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        return 0.0
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    result = trapezoid_area(10, 20, 5)
    print(result)