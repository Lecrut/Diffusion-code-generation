def calculate_rhombus_area(d1, d2):
    if d1 < 0 or d2 < 0:
        raise ValueError("Diagonal lengths must be non-negative")
    return 0.5 * d1 * d2

if __name__ == '__main__':
    print(calculate_rhombus_area(4, 6))
    print(calculate_rhombus_area(5, 5))
    print(calculate_rhombus_area(0, 10))
    try:
        calculate_rhombus_area(-3, 5)
    except ValueError as e:
        print(str(e))