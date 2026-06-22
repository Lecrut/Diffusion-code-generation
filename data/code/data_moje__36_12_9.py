def calculate_trapezoid_area(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    base1 = 10
    base2 = 20
    height = 5
    area = calculate_trapezoid_area(base1, base2, height)
    print(area)