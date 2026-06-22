def calculate_rhombus_area(diagonal1, diagonal2):
    if diagonal1 <= 0 or diagonal2 <= 0:
        raise ValueError("Diagonal lengths must be positive numbers")
    return 0.5 * diagonal1 * diagonal2

if __name__ == '__main__':
    print(calculate_rhombus_area(4, 6))
    print(calculate_rhombus_area(10, 10))
    try:
        calculate_rhombus_area(-1, 5)
    except ValueError as e:
        print(e)
    try:
        calculate_rhombus_area(0, 5)
    except ValueError as e:
        print(e)