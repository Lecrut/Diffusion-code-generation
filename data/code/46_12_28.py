def calculate_triangle_perimeter(side1, side2, side3):
    if not all((isinstance(x, (int, float)) for x in [side1, side2, side3])):
        raise TypeError('All sides must be numbers.')
    if any((x <= 0 for x in [side1, side2, side3])):
        raise ValueError('All sides must be positive numbers.')
    return side1 + side2 + side3
if __name__ == '__main__':
    try:
        print(calculate_triangle_perimeter(3, 4, 5))
        print(calculate_triangle_perimeter(7, 8, 9))
        print(calculate_triangle_perimeter(-1, 4, 5))
    except (ValueError, TypeError) as e:
        print(e)