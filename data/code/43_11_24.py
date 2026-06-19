def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    sample_values = {
        'small': 3,
        'medium': 5,
        'large': 7.2
    }
    
    for description, value in sample_values.items():
        area = calculate_square_area(value)
        print(f"The area of a square with {description} side length ({value}) is: {area}")