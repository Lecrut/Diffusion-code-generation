RHOMBUS_AREA_CONSTANT = 4

def calculate_rhombus_area(diag1: int, diag2: int) -> int:
    return (diag1 * diag2) // RHOMBUS_AREA_CONSTANT

def calculate_square_area(side_length: int) -> int:
    return side_length ** 2

def rhombus_square_areas_equal(diag1: int, diag2: int, side_length: int) -> bool:
    area_rhombus = calculate_rhombus_area(diag1, diag2)
    area_square = calculate_square_area(side_length)
    return area_rhombus == area_square

if __name__ == '__main__':
    print(rhombus_square_areas_equal(8, 6, 5))