def calculate_area(width: float, height: float) -> float:
    return width * height

if __name__ == '__main__':
    sample_width = 5.0
    sample_height = 3.0
    area = calculate_area(sample_width, sample_height)
    print(area)