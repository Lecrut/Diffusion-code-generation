import math

def herons_formula(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle: sum of any two sides must be greater than the third side.")
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

if __name__ == '__main__':
    print(herons_formula(3, 4, 5))