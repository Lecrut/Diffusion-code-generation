def validate_dimensions(w, h):
    return w > 0 and h > 0

def calculate_area(width, height):
    if not validate_dimensions(width, height):
        raise ValueError("Dimensions must be positive")
    return width * height

if __name__ == '__main__':
    w = 7
    h = 9
    print(calculate_area(w, h))