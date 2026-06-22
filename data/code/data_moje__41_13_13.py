def calculate_rhombus_area(d1, d2):
    if d1 < 0 or d2 < 0:
        raise ValueError("Diagonal lengths must be non-negative")
    return 0.5 * d1 * d2

if __name__ == '__main__':
    print(calculate_rhombus_area(10, 20))
    print(calculate_rhombus_area(5, 5))
    print(calculate_rhombus_area(0, 10))