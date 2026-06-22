def trapezoid_area(base1, base2, height):
    if height < 0:
        raise ValueError("Height must be non-negative")
    if base1 < 0 or base2 < 0:
        raise ValueError("Bases must be non-negative")
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    print(trapezoid_area(5, 10, 4))
    print(trapezoid_area(0, 0, 0))
    print(trapezoid_area(3.5, 7.5, 4.0))