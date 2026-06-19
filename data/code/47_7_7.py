def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

if __name__ == '__main__':
    try:
        area = calculate_area(9, 4)
        print(area)
    except ValueError as e:
        print(e)