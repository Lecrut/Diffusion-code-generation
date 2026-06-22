def calculate_area(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise ValueError("Both length and width must be numbers.")
    return length * width

if __name__ == '__main__':
    length_val = 10.5
    width_val = 5.0
    area = calculate_area(length_val, width_val)
    print(area)