def compute_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    base_one = 10
    base_two = 6
    height = 4
    area = compute_trapezoid_area(base_one, base_two, height)
    print(area)