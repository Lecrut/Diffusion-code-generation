def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Side length must be a numeric value.")
    area = side_length * side_length
    return area

if __name__ == '__main__':
    try:
        side1 = 8
        area1 = calculate_square_area(side1)
        print(f"The area of the square with side {side1} is: {area1}")
        
        side2 = 4.2
        area2 = calculate_square_area(side2)
        print(f"The area of the square with side {side2} is: {area2}")
        
        invalid_side = 'x'
        area3 = calculate_square_area(invalid_side)
        print(area3)
    except ValueError as e:
        print(e)