def calculate_area(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative numbers.")
    return length * width

if __name__ == '__main__':
    try:
        area = calculate_area(10.5, 5.0)
        print(area)
    except ValueError as e:
        print(e)