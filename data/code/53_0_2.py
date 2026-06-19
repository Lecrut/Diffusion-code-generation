def calculate_square_area(side_length):
    area = side_length ** 2
    return area

if __name__ == '__main__':
    sample_values = {'small': 3, 'medium': 7, 'large': 10}
    for size, value in sample_values.items():
        area = calculate_square_area(value)
        print(f"The area of a square with side length {value} is {area}.")