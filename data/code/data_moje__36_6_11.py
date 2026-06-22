def trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2
if __name__ == '__main__':
    base_one = 5.0
    base_two = 7.0
    height = 4.0
    area = trapezoid_area(base_one, base_two, height)
    print(area)