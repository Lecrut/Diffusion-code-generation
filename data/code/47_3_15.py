def herons_formula(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The sum of any two sides must be greater than the third side.")
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

if __name__ == '__main__':
    try:
        side1 = 6
        side2 = 8
        side3 = 10
        triangle_area = herons_formula(side1, side2, side3)
        print(f"The area of the triangle with sides {side1}, {side2}, and {side3} is: {triangle_area}")
    except ValueError as e:
        print(e)