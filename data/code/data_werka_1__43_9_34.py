def calculate_square_area(side_length):
    return side_length ** 2

if __name__ == '__main__':
    sample_values = {'small': 3, 'medium': 5, 'large': 7}
    area = calculate_square_area(sample_values['medium'])
    print(f"The area of a medium square with side length {sample_values['medium']} is {area}")