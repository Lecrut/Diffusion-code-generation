def calculate_rhombus_area(diagonal1, diagonal2):
    if not isinstance(diagonal1, (int, float)) or not isinstance(diagonal2, (int, float)):
        raise ValueError("Diagonals must be numbers.")
    if diagonal1 <= 0 or diagonal2 <= 0:
        raise ValueError("Diagonals must be positive.")
    return 0.5 * diagonal1 * diagonal2

def calculate_area_sum():
    area1 = calculate_rhombus_area(6, 8)
    area2 = calculate_rhombus_area(10, 12)
    return area1 + area2

if __name__ == '__main__':
    result = calculate_area_sum()
    print(result)