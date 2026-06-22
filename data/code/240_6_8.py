def calculate_square_area(side):
    return side * side

if __name__ == '__main__':
    sample_values = {1: 5.0, 2: 7.5, 3: 9.0}
    for key, value in sample_values.items():
        area = calculate_square_area(value)
        print(f"Test {key}: Side length is {value}, Area is {area}")