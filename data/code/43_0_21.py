def calculate_square_area(side):
    return side * side

if __name__ == '__main__':
    sample_values = {
        'small': 3,
        'medium': 5,
        'large': 10
    }
    
    for size, side_length in sample_values.items():
        area = calculate_square_area(side_length)
        print(f"The area of a {size} square with side length {side_length} is {area}.")