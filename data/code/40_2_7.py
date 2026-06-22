def calculate_surface_area(length: float, width: float, height: float) -> float:
    if length < 0 or width < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    sample_length = 5.0
    sample_width = 3.0
    sample_height = 4.0
    result = calculate_surface_area(sample_length, sample_width, sample_height)
    print(result)