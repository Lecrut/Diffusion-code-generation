def calculate_area(length: float | int, width: float | int) -> float:
    return float(length * width)
if __name__ == '__main__':
    print(calculate_area(5, 10))
    print(calculate_area(3.5, 4))
    print(calculate_area(7, 2.5))
    print(calculate_area(10, 10))