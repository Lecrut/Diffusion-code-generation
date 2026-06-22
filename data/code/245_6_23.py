def rhombus_square_areas_equal(diag1: int, diag2: int, side_length: int) -> bool:
    if not all(isinstance(i, int) for i in [diag1, diag2, side_length]):
        raise ValueError("All inputs must be integers.")
    if side_length <= 0 or diag1 <= 0 or diag2 <= 0:
        raise ValueError("Side length and diagonals must be positive numbers.")
    
    area_rhombus = (diag1 * diag2) // 4
    area_square = side_length ** 2
    
    return area_rhombus == area_square

if __name__ == '__main__':
    try:
        print(rhombus_square_areas_equal(8, 6, 5))
    except ValueError as e:
        print(e)