def calculate_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Invalid input type for side length")
    return side_length * side_length

if __name__ == '__main__':
    sample_values = [5, 10.5]
    for value in sample_values:
        area = calculate_area(value)
        print(f"Area of square with side length {value}: {area}")