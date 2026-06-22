def calculate_trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    result = calculate_trapezoid_area(10, 15, 8)
    print(result)