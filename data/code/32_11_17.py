def compute_area(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Dimensions must be numeric")
    if width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive")
    return width * height

if __name__ == '__main__':
    w = 7
    h = 4
    print(compute_area(w, h))