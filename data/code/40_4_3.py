def calculate_rectangular_surface_area(length: float, width: float, height: float) -> float:
    if length < 0 or width < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    length = 5
    width = 4
    height = 3
    area = calculate_rectangular_surface_area(length, width, height)
    print(area)