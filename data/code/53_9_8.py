def calculate_square_area(side_length):
    return side_length ** 2

if __name__ == '__main__':
    sample_values = [4, 7, 15]
    for value in sample_values:
        area = calculate_square_area(value)
        print(f"The area of a square with side length {value} is {area}.")