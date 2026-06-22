def calculate_area(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise ValueError("Length and width must be numbers")
    return length * width

if __name__ == '__main__':
    try:
        area = calculate_area(10, 5)
        print(area)
    except ValueError as e:
        print(e)