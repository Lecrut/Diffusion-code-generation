def calculate_surface_area(length: float, width: float, height: float) -> float:
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    result = calculate_surface_area(2.5, 3.0, 4.0)
    print(result)