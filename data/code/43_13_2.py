def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    sample_values = {'side1': 3, 'side2': 4, 'side3': 5}
    for name, side in sample_values.items():
        area = calculate_square_area(side)
        print(f"The area of the square with {name} side length is: {area}")