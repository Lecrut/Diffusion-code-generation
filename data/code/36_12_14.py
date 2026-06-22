def trapezoid_area(base1, base2, height):
    if height < 0:
        raise ValueError("Height must be non-negative")
    if base1 < 0 or base2 < 0:
        raise ValueError("Bases must be non-negative")
    if height == 0:
        return 0.0
    average_base = (base1 + base2) * 0.5
    return average_base * height

if __name__ == '__main__':
    result = trapezoid_area(5, 7, 4)
    print(result)