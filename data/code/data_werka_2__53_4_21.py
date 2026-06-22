def calculate_area(side):
    return side * side

if __name__ == '__main__':
    sample_values = {'side1': 3, 'side2': 7, 'side3': 10}
    for name, side in sample_values.items():
        print(f"The area of the square with {name} is: {calculate_area(side)}")