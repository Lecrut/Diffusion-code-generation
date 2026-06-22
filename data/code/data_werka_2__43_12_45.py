def calculate_square_area(side_length):
    def validate_side_length(length):
        if length < 0:
            raise ValueError("Side length cannot be negative")
    
    validate_side_length(side_length)
    return side_length ** 2

if __name__ == '__main__':
    sample_values = [
        {'size': 'small', 'length': 4},
        {'size': 'medium', 'length': 9},
        {'size': 'large', 'length': 15}
    ]
    for value in sample_values:
        area = calculate_square_area(value['length'])
        print(f"The area of a {value['size']} square with side length {value['length']} is {area}")