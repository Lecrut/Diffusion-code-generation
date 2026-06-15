def calculate_square_area(side):
    area = side * side
    return area
if __name__ == '__main__':
    sample_side = 5
    try:
        input_side = int(sample_side)
        if input_side < 0:
            raise ValueError("Side length cannot be negative.")
        area = calculate_square_area(input_side)
        print(f"The side length entered is: {input_side}")
        print(f"The area of the square is: {area}")
    except ValueError as e:
        print(f"Error: Invalid input. {e}")
    except TypeError:
        print("Error: Input must be an integer.")