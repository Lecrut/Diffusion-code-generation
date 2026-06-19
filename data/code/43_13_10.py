def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    sample_values = {
        'small': 2,
        'medium': 5,
        'large': 10
    }
    for description, side in sample_values.items():
        area = calculate_square_area(side)
        print(f"The area of the {description} square with side length {side} is: {area}")