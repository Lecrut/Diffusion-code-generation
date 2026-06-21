def calculate_square_area(side_length):
    if side_length <= 0:
        raise ValueError('Side length must be positive')
    area = side_length * side_length
    return area

if __name__ == '__main__':
    try:
        side1 = 4
        print(f"The area of a square with side {side1} is: {calculate_square_area(side1)}")
        
        side2 = -5
        print(f"The area of a square with side {side2} is: {calculate_square_area(side2)}")
    except ValueError as e:
        print(e)