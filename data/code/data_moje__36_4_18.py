def trapezoid_area(base1, base2, height):
    if height <= 0:
        return 0.0
    if base1 <= 0 or base2 <= 0:
        return 0.0
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    FIRST_BASE = 12
    SECOND_BASE = 18
    PERPENDICULAR_HEIGHT = 6
    result = trapezoid_area(FIRST_BASE, SECOND_BASE, PERPENDICULAR_HEIGHT)
    print(result)