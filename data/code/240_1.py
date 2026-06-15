def calculate_square_area(side: float | int) -> float:
    return side * side
if __name__ == '__main__':
    side1 = 5.0
    area1 = calculate_square_area(side1)
    print(f"The area of a square with side {side1} is: {area1}")
    side2 = 10
    area2 = calculate_square_area(side2)
    print(f"The area of a square with side {side2} is: {area2}")
    side3 = 3.5
    area3 = calculate_square_area(side3)
    print(f"The area of a square with side {side3} is: {area3}")