def compute_rhombus_area(d1, d2):
    if not isinstance(d1, (int, float)) or not isinstance(d2, (int, float)):
        raise TypeError("Diagonals must be numeric")
    if d1 <= 0 or d2 <= 0:
        raise ValueError("Diagonals must be positive")
    return d1 * d2 * 0.5

if __name__ == '__main__':
    diag_1 = 12
    diag_2 = 16
    area_value = compute_rhombus_area(diag_1, diag_2)
    print(area_value)