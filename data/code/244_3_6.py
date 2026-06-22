def trapezoid_area(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Base and height must be non-negative.")
    return 0.5 * (base1 + base2) * height

def parallelogram_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative.")
    return base * height

if __name__ == '__main__':
    trapezoid = trapezoid_area(5, 7, 4)
    parallelogram = parallelogram_area(6, 3)
    print(trapezoid + parallelogram)