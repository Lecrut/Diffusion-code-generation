def trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    base1_value = 10
    base2_value = 15
    height_value = 6
    result = trapezoid_area(base1_value, base2_value, height_value)
    print(result)