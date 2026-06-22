def calculate_rectangular_surface_area(length: float, width: float, height: float) -> float:
    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive")
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    l, w, h = 10, 5, 3
    area = calculate_rectangular_surface_area(l, w, h)
    print(area)