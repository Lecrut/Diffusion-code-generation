def calculate_triangle_area(base, height):
    try:
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        area = 0.5 * base * height
        return area
    except TypeError:
        raise TypeError("Both base and height must be floating-point numbers.")

if __name__ == '__main__':
    base_value = 10.0
    height_value = 5.0
    try:
        result = calculate_triangle_area(base_value, height_value)
        print(result)
    except Exception as e:
        print(e)