def rhombus_square_areas_equal(d1: int, d2: int, side_length: int) -> bool:
    return (d1 * d2) // 4 == side_length ** 2

if __name__ == '__main__':
    print(rhombus_square_areas_equal(8, 6, 5))