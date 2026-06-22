def calculate_triangle_perimeter(a, b, c):
    side_map = {'a': a, 'b': b, 'c': c}
    if any(side <= 0 for side in side_map.values()):
        raise ValueError('Sides must be positive numbers')
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError('The given sides do not form a valid triangle')
    return sum(side_map.values())

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(5.0, 12.0, 13.0)
        print(perimeter)
    except ValueError as e:
        print(e)