def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    test_cases = {
        'tiny': 1,
        'small': 2,
        'medium': 3,
        'large': 4,
        'huge': 5
    }
    
    for description, length in test_cases.items():
        area_result = calculate_square_area(length)
        print(f"The area of a {description} square with side length {length} is {area_result}.")