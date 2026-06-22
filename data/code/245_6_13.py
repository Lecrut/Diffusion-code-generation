def rhombus_square_areas_equal(d1: int, d2: int, side_length: int) -> bool:
    area_rhombus = (d1 * d2) // 4
    area_square = side_length ** 2
    return area_rhombus == area_square

if __name__ == '__main__':
    print(rhombus_square_areas_equal(8, 6, 5))