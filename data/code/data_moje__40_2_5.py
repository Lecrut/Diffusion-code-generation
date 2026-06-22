def calculate_surface_area(length: float, width: float, height: float) -> float:
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    result = calculate_surface_area(3.0, 4.0, 5.0)
    print(result)