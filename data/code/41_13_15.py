def calculate_rhombus_area(diagonal1, diagonal2):
    if diagonal1 < 0 or diagonal2 < 0:
        raise ValueError("Diagonal lengths must be non-negative")
    return 0.5 * diagonal1 * diagonal2

if __name__ == '__main__':
    print(calculate_rhombus_area(10, 20))
    print(calculate_rhombus_area(5, 5))
    print(calculate_rhombus_area(0, 10))