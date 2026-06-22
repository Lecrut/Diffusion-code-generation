def calculate_rectangular_container_surface_area(length, width, height):
    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive numbers.")
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    length = 10.0
    width = 5.0
    height = 3.0
    result = calculate_rectangular_container_surface_area(length, width, height)
    print(result)