def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def parallelogram_area(base, height):
    return base * height

if __name__ == '__main__':
    trapezoid_result = trapezoid_area(5, 7, 4)
    parallelogram_result = parallelogram_area(6, 3)
    print(trapezoid_result + parallelogram_result)