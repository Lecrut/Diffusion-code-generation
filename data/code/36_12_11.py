def trapezoid_area(b1, b2, height):
    if b1 < 0 or b2 < 0 or height < 0:
        raise ValueError('Bases and height must be non-negative.')
    area = 0.5 * (b1 + b2) * height
    return area
if __name__ == '__main__':
    b1 = 5.0
    b2 = 7.0
    height = 4.0
    area = trapezoid_area(b1, b2, height)
    print(area)