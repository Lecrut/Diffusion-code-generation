def trapezoid_area(base1, base2, height):
    if not (isinstance(base1, (int, float)) and isinstance(base2, (int, float)) and isinstance(height, (int, float))):
        raise ValueError("All inputs must be numbers")
    return 0.5 * (base1 + base2) * height

def parallelogram_area(base, height):
    if not (isinstance(base, (int, float)) and isinstance(height, (int, float))):
        raise ValueError("Both base and height must be numbers")
    return base * height

if __name__ == '__main__':
    trapezoid = trapezoid_area(5, 7, 4)
    parallelogram = parallelogram_area(6, 3)
    print(trapezoid + parallelogram)