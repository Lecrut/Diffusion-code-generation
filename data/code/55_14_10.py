def calculate_triangle_perimeter(a, b, c):
    for side in (a, b, c):
        if not isinstance(side, (int, float)):
            raise ValueError('All sides must be numeric types.')
        if side <= 0:
            raise ValueError('Side lengths must be positive numbers.')
    return a + b + c
if __name__ == '__main__':
    try:
        perimeter1 = calculate_triangle_perimeter(3, 4, 5)
        print(perimeter1)
        perimeter2 = calculate_triangle_perimeter(6.0, 8.0, 10.0)
        print(perimeter2)
        perimeter3 = calculate_triangle_perimeter(-1, 2, 3)
    except ValueError as e:
        print(e)