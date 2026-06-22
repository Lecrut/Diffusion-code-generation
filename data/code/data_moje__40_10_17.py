def validate_dimensions(length, width, height):
    if not isinstance(length, (int, float)) or length <= 0:
        raise ValueError("Length must be a positive number")
    if not isinstance(width, (int, float)) or width <= 0:
        raise ValueError("Width must be a positive number")
    if not isinstance(height, (int, float)) or height <= 0:
        raise ValueError("Height must be a positive number")

def calculate_surface_area(length, width, height):
    validate_dimensions(length, width, height)
    face_area_lw = length * width
    face_area_wh = width * height
    face_area_hl = height * length
    total = 2 * (face_area_lw + face_area_wh + face_area_hl)
    return total

if __name__ == '__main__':
    dim_length = 10
    dim_width = 5
    dim_height = 3
    computed_area = calculate_surface_area(dim_length, dim_width, dim_height)
    print(computed_area)