def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)) or side_length < 0:
        raise ValueError("Side length must be a non-negative number.")
    
    area = side_length ** 2
    return area

if __name__ == '__main__':
    sample_side_lengths = [3.5, 6, 9]
    for length in sample_side_lengths:
        try:
            area_result = calculate_square_area(length)
            print(f"The area of a square with side length {length} is {area_result}.")
        except ValueError as e:
            print(e)