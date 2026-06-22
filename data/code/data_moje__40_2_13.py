def calculate_surface_area(length: float, width: float, height: float) -> float:
    if length < 0 or width < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative.")
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    l = 5.0
    w = 3.0
    h = 4.0
    result = calculate_surface_area(l, w, h)
    print(result)