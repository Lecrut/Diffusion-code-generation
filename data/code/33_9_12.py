def sanitize_input(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        raise TypeError("Input must be a numeric type")

def compute_triangle_area(base, height):
    sanitized_base = sanitize_input(base)
    sanitized_height = sanitize_input(height)
    if sanitized_base < 0 or sanitized_height < 0:
        raise ValueError("Base and height must be non-negative")
    return 0.5 * sanitized_base * sanitized_height

if __name__ == '__main__':
    result = compute_triangle_area(10, 5)
    print(result)
    result_float = compute_triangle_area(7.5, 4.2)
    print(result_float)
    try:
        compute_triangle_area("ten", 5)
    except TypeError:
        print("Caught TypeError for non-numeric base")
    try:
        compute_triangle_area(10, -2)
    except ValueError:
        print("Caught ValueError for negative height")