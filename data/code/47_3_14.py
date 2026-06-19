TRIANGLE_SIDES_THRESHOLD = 1e-9

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def herons_formula(a, b, c):
    if not is_valid_triangle(a, b, c):
        raise ValueError("Invalid triangle sides")
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

if __name__ == '__main__':
    try:
        side1 = 3.0
        side2 = 4.0
        side3 = 5.0
        print(herons_formula(side1, side2, side3))
    except ValueError as e:
        print(e)