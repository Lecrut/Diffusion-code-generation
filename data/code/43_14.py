def calculate_square_area(side):
    if side <= 0:
        raise ValueError("Side length must be a positive number.")
    return side * side
if __name__ == '__main__':
    side1 = 5
    side2 = 10.5
    side3 = -3
    side4 = 0
    try:
        area1 = calculate_square_area(side1)
        print(f"The area of a square with side {side1} is: {area1}")
        area2 = calculate_square_area(side2)
        print(f"The area of a square with side {side2} is: {area2}")
        area3 = calculate_square_area(side3)
    except ValueError as e:
        print(f"Error for side {side3}: {e}")
    try:
        area4 = calculate_square_area(side4)
    except ValueError as e:
        print(f"Error for side {side4}: {e}")