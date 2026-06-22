def herons_formula(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle sides")
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

if __name__ == '__main__':
    try:
        side1 = 3
        side2 = 4
        side3 = 5
        print(herons_formula(side1, side2, side3))
    except ValueError as e:
        print(e)