def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Side length must be a numeric value.")
    return side_length * side_length

if __name__ == '__main__':
    try:
        side1 = 4
        area1 = calculate_square_area(side1)
        print(f"The area of the square with side {side1} is: {area1}")

        side2 = 8.2
        area2 = calculate_square_area(side2)
        print(f"The area of the square with side {side2} is: {area2}")

        invalid_side = 'hello'
        area3 = calculate_square_area(invalid_side)
        print(area3)
    except ValueError as e:
        print(e)