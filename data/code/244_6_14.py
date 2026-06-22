DIAGONAL_MULTIPLIER = 0.5

def calculate_rhombus_area(diagonal1, diagonal2):
    return DIAGONAL_MULTIPLIER * diagonal1 * diagonal2

def calculate_area_sum():
    diag1_first = 6
    diag2_first = 8
    diag1_second = 10
    diag2_second = 12
    area_first = calculate_rhombus_area(diag1_first, diag2_first)
    area_second = calculate_rhombus_area(diag1_second, diag2_second)
    return area_first + area_second
if __name__ == '__main__':
    result = calculate_area_sum()
    print(result)