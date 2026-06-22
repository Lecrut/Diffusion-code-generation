def calculate_rhombus_area(d1, d2):
    if d1 <= 0 or d2 <= 0:
        raise ValueError("Diagonals must be positive")
    return (d1 * d2) / 2

if __name__ == '__main__':
    d1 = 10
    d2 = 8
    result = calculate_rhombus_area(d1, d2)
    print(result)