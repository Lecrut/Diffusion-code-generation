def calculate_rhombus_area(diagonal_1, diagonal_2):
    if diagonal_1 <= 0 or diagonal_2 <= 0:
        raise ValueError("Diagonal lengths must be positive numbers.")
    return (diagonal_1 * diagonal_2) / 2

if __name__ == '__main__':
    d1 = 10
    d2 = 15
    result = calculate_rhombus_area(d1, d2)
    print(result)
    try:
        calculate_rhombus_area(0, 5)
    except ValueError as e:
        print(e)
    try:
        calculate_rhombus_area(-3, 7)
    except ValueError as e:
        print(e)