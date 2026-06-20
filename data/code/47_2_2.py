def triangle_area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The side lengths do not form a valid triangle")
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

if __name__ == '__main__':
    print(triangle_area(3, 4, 5))
    print(triangle_area(5, 12, 13))
    print(triangle_area(7, 8, 9))