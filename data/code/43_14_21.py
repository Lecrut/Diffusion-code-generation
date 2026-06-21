def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError('Side length must be a numeric value.')
    if side_length < 0:
        raise ValueError('Side length cannot be negative.')
    area = side_length * side_length
    return area

if __name__ == '__main__':
    try:
        sample_side_1 = 7
        sample_side_2 = 4.8
        sample_side_3 = -5
        
        print(f"Area of square with side {sample_side_1}: {calculate_square_area(sample_side_1)}")
        print(f"Area of square with side {sample_side_2}: {calculate_square_area(sample_side_2)}")
        print(f"Area of square with side {sample_side_3}: {calculate_square_area(sample_side_3)}")
    except ValueError as e:
        print(e)