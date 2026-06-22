def calculate_trapezoid_area(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Base lengths and height must be non-negative")
    if height == 0 and (base1 == 0 or base2 == 0):
        return 0
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    base1 = 5
    base2 = 7
    height = 4
    result = calculate_trapezoid_area(base1, base2, height)
    print(result)
    result2 = calculate_trapezoid_area(10, 20, 5)
    print(result2)
    result3 = calculate_trapezoid_area(0, 5, 10)
    print(result3)