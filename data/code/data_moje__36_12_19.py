def trapezoid_area(base1, base2, height):
    if height <= 0:
        raise ValueError("Height must be positive")
    return ((base1 + base2) / 2.0) * height

if __name__ == '__main__':
    result = trapezoid_area(5.0, 10.0, 4.0)
    print(result)