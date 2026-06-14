def calculate_square_area(side):
    try:
        side = float(side)
        if side < 0:
            raise ValueError("Side cannot be negative")
        return side * side
    except ValueError as e:
        return f"Error: Invalid input. {e}"
if __name__ == '__main__':
    sample_inputs = [10, 5.5, "abc", -3]
    for input_val in sample_inputs:
        result = calculate_square_area(input_val)
        print(f"Input: {input_val}, Area: {result}")