def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length must be a non-negative number.")
    return side_length * side_length

if __name__ == '__main__':
    sample_values = {
        'tiny': 1,
        'small': 3,
        'medium': 5,
        'large': 7,
        'huge': 9
    }
    
    for size, length in sample_values.items():
        try:
            area = calculate_square_area(length)
            print(f"The area of a {size} square with side length {length} is {area}.")
        except ValueError as e:
            print(e)