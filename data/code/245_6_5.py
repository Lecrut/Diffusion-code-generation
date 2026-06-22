def rhombus_square_areas_equal(diag1, diag2, side):
    area_rhombus = (diag1 * diag2) // 4
    area_square = side ** 2
    return area_rhombus == area_square

if __name__ == '__main__':
    print(rhombus_square_areas_equal(8, 6, 5))