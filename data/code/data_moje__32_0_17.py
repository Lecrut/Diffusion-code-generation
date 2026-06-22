def _validate_dimension(value, name):
    if value < 0:
        raise ValueError(f"{name} cannot be negative")

def calculate_rectangle_area(width, height):
    _validate_dimension(width, "Width")
    _validate_dimension(height, "Height")
    return width * height

if __name__ == '__main__':
    w_val = 12
    h_val = 7
    print(calculate_rectangle_area(w_val, h_val))