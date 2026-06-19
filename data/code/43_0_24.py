def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise ValueError("Side length must be a number.")
    if side < 0:
        raise ValueError("Side length cannot be negative.")
    
    area = side * side
    return area

if __name__ == '__main__':
    sample_sides = [3, 5, 10]
    for side_length in sample_sides:
        try:
            area_result = calculate_square_area(side_length)
            print(f"The area of a square with side length {side_length} is {area_result}.")
        except ValueError as e:
            print(e)