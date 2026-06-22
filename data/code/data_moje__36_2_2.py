def trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    base1_value = 5
    base2_value = 7
    height_value = 4
    area = trapezoid_area(base1_value, base2_value, height_value)
    print(area)