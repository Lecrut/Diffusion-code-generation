def validate_dimensions(dims):
    for d in dims:
        if not isinstance(d, (int, float)):
            raise TypeError("Dimensions must be numeric")
        if d <= 0:
            raise ValueError("Dimensions must be positive")

def box_surface_area(length, width, height):
    validate_dimensions([length, width, height])
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    print(box_surface_area(10, 8, 6))