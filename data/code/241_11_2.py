def calculate_rectangle_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
if __name__ == '__main__':
    print(calculate_rectangle_area(5, 10))
    try:
        calculate_rectangle_area(-5, 10)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        calculate_rectangle_area(5, 0)
    except ValueError as e:
        print(f"Error caught: {e}")
    print(calculate_rectangle_area(3.5, 2))