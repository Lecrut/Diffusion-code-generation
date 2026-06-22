def calculate_rhombus_area(d1: float, d2: float) -> float:
    if d1 <= 0:
        raise ValueError("First diagonal length must be positive")
    if d2 <= 0:
        raise ValueError("Second diagonal length must be positive")
    return (d1 * d2) / 2

if __name__ == '__main__':
    result = calculate_rhombus_area(10, 6)
    print(result)