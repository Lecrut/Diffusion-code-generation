def calculate_square_area(side_length):
    return side_length ** 2

if __name__ == '__main__':
    sample_values = {
        'small': 3,
        'medium': 5,
        'large': 7
    }
    
    for size, value in sample_values.items():
        area = calculate_square_area(value)
        print(f"The area of the {size} square with side {value} is {area}")