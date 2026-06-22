DIAGONAL_FACTOR = {"rhombus": 0.5}

compute_rhombus_area = lambda d1, d2: DIAGONAL_FACTOR["rhombus"] * d1 * d2

if __name__ == '__main__':
    print(compute_rhombus_area(6.0, 8.0))