def calculate_heron_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle sides")
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

if __name__ == '__main__':
    try:
        side1 = 6
        side2 = 8
        side3 = 10
        print(calculate_heron_area(side1, side2, side3))
    except ValueError as e:
        print(e)