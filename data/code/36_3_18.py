def calculate_trapezoid_area(base1, base2, height):
    return (base1 + base2) / 2 * height

if __name__ == '__main__':
    area1 = calculate_trapezoid_area(5, 10, 4)
    print(area1)
    area2 = calculate_trapezoid_area(3, 7, 2)
    print(area2)
    area3 = calculate_trapezoid_area(1, 1, 1)
    print(area3)