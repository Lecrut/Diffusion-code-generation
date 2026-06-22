def calculate_rhombus_area(diag1: int, diag2: int) -> int:
    return (diag1 * diag2) // 4

def calculate_square_area(side_length: int) -> int:
    return side_length ** 2

def rhombus_square_areas_equal(diag1: int, diag2: int, side_length: int) -> bool:
    area_rhombus = calculate_rhombus_area(diag1, diag2)
    area_square = calculate_square_area(side_length)
    return area_rhombus == area_square

if __name__ == '__main__':
    diag1_sample = 10
    diag2_sample = 6
    side_length_sample = 5
    print(rhombus_square_areas_equal(diag1_sample, diag2_sample, side_length_sample))