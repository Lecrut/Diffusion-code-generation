def calculate_rhombus_area(diagonal1: float, diagonal2: float) -> float:
    return (diagonal1 * diagonal2) / 2

if __name__ == '__main__':
    result = calculate_rhombus_area(5.0, 10.0)
    print(result)