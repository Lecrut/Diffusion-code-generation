def calculate_triangle_area(base, height):
    try:
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        area = 0.5 * base * height
        return area
    except TypeError as e:
        print(f"TypeError: {e}")
        return None
    except ValueError as e:
        print(f"ValueError: {e}")
        return None

if __name__ == '__main__':
    base_value = 10.0
    height_value = 5.0
    area = calculate_triangle_area(base_value, height_value)
    if area is not None:
        print(area)