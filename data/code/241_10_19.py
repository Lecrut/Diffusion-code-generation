def calculate_area(width: float, height: float) -> float:
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative numbers")
    return width * height

if __name__ == '__main__':
    sample_width = 8.0
    sample_height = 3.5
    result = calculate_area(sample_width, sample_height)
    print(result)