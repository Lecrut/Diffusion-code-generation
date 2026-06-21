def calculate_area_with_heron(sides):
    if len(sides) != 3:
        raise ValueError('Exactly three sides are required to form a triangle.')
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('Side lengths must be positive numbers.')
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The given sides do not form a valid triangle.')
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
if __name__ == '__main__':
    try:
        sides = [3, 4, 5]
        area = calculate_area_with_heron(sides)
        print(area)
    except ValueError as e:
        print(e)