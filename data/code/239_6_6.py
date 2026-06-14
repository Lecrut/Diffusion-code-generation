def calculate_rectangle_perimeter(length, width):
    try:
        length = float(length)
        width = float(width)
        if length < 0 or width < 0:
            raise ValueError("Dimensions cannot be negative")
        return 2 * (length + width)
    except ValueError as e:
        raise TypeError(f"Invalid input type or value: {e}") from e
    except Exception as e:
        raise TypeError(f"An unexpected error occurred: {e}") from e
if __name__ == '__main__':
    print(calculate_rectangle_perimeter(10, 5))
    try:
        calculate_rectangle_perimeter("ten", 5)
    except TypeError as e:
        print(f"Error caught: {e}")
    try:
        calculate_rectangle_perimeter(10, "five")
    except TypeError as e:
        print(f"Error caught: {e}")
    try:
        calculate_rectangle_perimeter(-10, 5)
    except TypeError as e:
        print(f"Error caught: {e}")