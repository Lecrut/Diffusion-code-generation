def calculate_triangle_area(base, height):
    def validate_input(b, h):
        if not isinstance(b, (float, int)) or not isinstance(h, (float, int)):
            raise TypeError("Both base and height must be numbers.")
        if b <= 0 or h <= 0:
            raise ValueError("Base and height must be positive numbers.")

    try:
        validate_input(base, height)
        area = 0.5 * base * height
        return area
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_base = 7.5
    sample_height = 4.2
    result = calculate_triangle_area(sample_base, sample_height)
    if result is not None:
        print(result)