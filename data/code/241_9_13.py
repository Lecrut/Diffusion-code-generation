def calculate_area(length, width):
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
        raise ValueError("Both length and width must be numbers.")
    return length * width

if __name__ == '__main__':
    try:
        area = calculate_area(5, 3)
        print(area)
    except ValueError as e:
        print(e)