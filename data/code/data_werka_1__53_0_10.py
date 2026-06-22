def calculate_square_area(side_length):
    area = side_length ** 2
    return area

if __name__ == '__main__':
    sample_values = {
        'tiny': 1,
        'small': 3,
        'medium': 5,
        'large': 7,
        'huge': 10
    }
    for size, value in sample_values.items():
        area = calculate_square_area(value)
        print(f"The area of a {size} square with side length {value} is {area}.")