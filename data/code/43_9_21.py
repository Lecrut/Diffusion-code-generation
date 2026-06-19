def calculate_square_area(side_length):
    return side_length ** 2

if __name__ == '__main__':
    sample_values = {'side1': 3, 'side2': 4.5}
    for name, side in sample_values.items():
        area = calculate_square_area(side)
        print(f"Area of square with {name} side: {area}")