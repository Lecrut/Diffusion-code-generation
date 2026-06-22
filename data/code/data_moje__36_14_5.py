def calculate_trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    base1 = 5
    base2 = 7
    height = 4
    result = calculate_trapezoid_area(base1, base2, height)
    print(result)