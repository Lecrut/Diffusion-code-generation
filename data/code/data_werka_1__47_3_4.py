def herons_formula(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle sides")
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

if __name__ == '__main__':
    try:
        print(herons_formula(6, 8, 10))
    except ValueError as e:
        print(e)