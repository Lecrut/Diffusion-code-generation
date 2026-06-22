def calculate_rhombus_area(diagonal1, diagonal2):
    if diagonal1 < 0 or diagonal2 < 0:
        raise ValueError("Diagonal lengths must be non-negative")
    if diagonal1 == 0 or diagonal2 == 0:
        raise ValueError("Diagonal lengths must be positive")
    return 0.5 * diagonal1 * diagonal2

if __name__ == '__main__':
    d1 = 10
    d2 = 8
    area = calculate_rhombus_area(d1, d2)
    print(area)