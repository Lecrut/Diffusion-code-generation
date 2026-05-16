def calculate_triangle_area(base, height):
    try:
        base_float = float(base)
        height_float = float(height)
        if base_float <= 0 or height_float <= 0:
            return "Error: Base and height must be positive values."
        area = 0.5 * base_float * height_float
        return f"{area:.2f}"
    except ValueError:
        return "Error: Invalid input. Please enter numeric values."
if __name__ == '__main__':
    base_input = "10.5"
    height_input = "4.0"
    result = calculate_triangle_area(base_input, height_input)
    print(result)