def calculate_rhombus_area(d1, d2):
    if d1 < 0 or d2 < 0:
        raise ValueError("Diagonals must be non-negative")
    return 0.5 * d1 * d2

if __name__ == '__main__':
    d1_val = 10.0
    d2_val = 6.0
    result = calculate_rhombus_area(d1_val, d2_val)
    print(result)