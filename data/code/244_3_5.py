def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def parallelogram_area(base, height):
    return base * height

if __name__ == '__main__':
    print(trapezoid_area(5, 7, 4))
    print(parallelogram_area(6, 3))