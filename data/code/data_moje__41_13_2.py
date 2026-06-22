def calculate_rhombus_area(d1, d2):
    if d1 < 0 or d2 < 0:
        raise ValueError("Diagonal lengths must be non-negative")
    if d1 == 0 or d2 == 0:
        raise ValueError("Diagonal lengths must be positive")
    return 0.5 * d1 * d2

if __name__ == '__main__':
    result = calculate_rhombus_area(6, 8)
    print(result)