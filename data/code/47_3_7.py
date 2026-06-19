def herons_formula(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The sum of any two sides must be greater than the third side.")
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

if __name__ == '__main__':
    try:
        triangle_sides = {'side1': 3, 'side2': 4, 'side3': 5}
        print(herons_formula(triangle_sides['side1'], triangle_sides['side2'], triangle_sides['side3']))
    except ValueError as e:
        print(e)