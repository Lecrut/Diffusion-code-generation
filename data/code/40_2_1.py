def calculate_rectangular_box_surface_area(length: float, width: float, height: float) -> float:
    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive numbers")
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    result = calculate_rectangular_box_surface_area(10, 5, 2)
    print(result)