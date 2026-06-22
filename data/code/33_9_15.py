def compute_triangle_area(base, height):
    try:
        base_num = float(base)
        height_num = float(height)
        if base_num < 0 or height_num < 0:
            raise ValueError("Base and height must be non-negative")
        return 0.5 * base_num * height_num
    except (TypeError, ValueError) as e:
        raise ValueError(f"Invalid input: {e}")

if __name__ == '__main__':
    result = compute_triangle_area(10, 5)
    print(result)
    invalid_result = None
    try:
        invalid_result = compute_triangle_area('a', 5)
    except ValueError as e:
        print(str(e))