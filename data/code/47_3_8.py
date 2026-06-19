def validate_triangle_sides(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The sum of any two sides must be greater than the third side.")

def herons_formula(a, b, c):
    validate_triangle_sides(a, b, c)
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

if __name__ == '__main__':
    try:
        side1 = 6
        side2 = 8
        side3 = 10
        print(herons_formula(side1, side2, side3))
    except ValueError as e:
        print(e)