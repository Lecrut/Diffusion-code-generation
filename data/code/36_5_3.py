def compute_trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    base1 = 5.0
    base2 = 7.0
    height = 4.0
    result = compute_trapezoid_area(base1, base2, height)
    print(result)