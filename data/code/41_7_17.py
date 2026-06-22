def calculate_rhombus_area(diagonal1, diagonal2):
    if not isinstance(diagonal1, (int, float)):
        raise TypeError('diagonal1 must be a number')
    if not isinstance(diagonal2, (int, float)):
        raise TypeError('diagonal2 must be a number')
    if diagonal1 <= 0:
        raise ValueError('diagonal1 must be positive')
    if diagonal2 <= 0:
        raise ValueError('diagonal2 must be positive')
    return 0.5 * diagonal1 * diagonal2
if __name__ == '__main__':
    d1 = 8.0
    d2 = 6.0
    area = calculate_rhombus_area(d1, d2)
    print(area)