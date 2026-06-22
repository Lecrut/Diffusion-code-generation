def trapezoid_area(base1, base2, height):
    if base1 <= 0 or base2 <= 0 or height <= 0:
        raise ValueError("All dimensions must be positive numbers.")
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    base1_value = 10
    base2_value = 6
    height_value = 4
    computed_area = trapezoid_area(base1_value, base2_value, height_value)
    print(computed_area)