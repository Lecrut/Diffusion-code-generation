def calculate_rhombus_area(d1, d2):
    if d1 <= 0 or d2 <= 0:
        raise ValueError("Diagonal lengths must be positive numbers.")
    return (d1 * d2) / 2

if __name__ == '__main__':
    print(calculate_rhombus_area(10, 5))
    print(calculate_rhombus_area(7.5, 4.2))