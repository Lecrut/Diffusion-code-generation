def area_of_trapezoid(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Base and height values must be non-negative")
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    result = area_of_trapezoid(10.0, 20.0, 5.0)
    print(result)