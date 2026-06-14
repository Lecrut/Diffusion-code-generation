def calculate_area(side1: float | int, side2: float | int) -> float:
    return float(side1 * side2)
if __name__ == '__main__':
    print(calculate_area(5, 4))
    print(calculate_area(3.5, 2))
    print(calculate_area(10, 7.5))
    print(calculate_area(1, 1))