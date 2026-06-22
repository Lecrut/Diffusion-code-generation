def calculate_rhombus_area(diagonal1, diagonal2):
    if diagonal1 <= 0 or diagonal2 <= 0:
        raise ValueError("Diagonals must be positive numbers")
    return 0.5 * diagonal1 * diagonal2

if __name__ == '__main__':
    result = calculate_rhombus_area(6, 8)
    print(result)