def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Side length must be a numeric value.")
    return side_length * side_length

if __name__ == '__main__':
    try:
        sample_values = [4, 5.5, 'a', None]
        for value in sample_values:
            area = calculate_square_area(value)
            print(f"The area of a square with side length {value} is {area}")
    except ValueError as e:
        print(e)