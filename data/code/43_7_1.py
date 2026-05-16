def calculate_square_area(side: float) -> float:
    return side * side
if __name__ == '__main__':
    side_value = 5.0
    area = calculate_square_area(side_value)
    print(f"The area of the square with side {side_value} is {area}")