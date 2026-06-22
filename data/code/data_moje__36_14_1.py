def calculate_trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2.0

if __name__ == '__main__':
    base1_value = 5.0
    base2_value = 7.0
    height_value = 4.0
    result = calculate_trapezoid_area(base1_value, base2_value, height_value)
    print(result)