def calculate_area(side1: float | int, side2: float | int) -> float:
    return float(side1 * side2)
if __name__ == '__main__':
    area1 = calculate_area(5, 4)
    print(f"Area of 5 and 4: {area1}")
    area2 = calculate_area(3.5, 2)
    print(f"Area of 3.5 and 2: {area2}")
    area3 = calculate_area(10, 10.5)
    print(f"Area of 10 and 10.5: {area3}")
    area4 = calculate_area(7, 8)
    print(f"Area of 7 and 8: {area4}")