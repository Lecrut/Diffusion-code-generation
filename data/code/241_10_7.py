def calculate_area(width: float, height: float) -> float:
    area = width * height
    return area

if __name__ == '__main__':
    sample_width = 8.0
    sample_height = 3.25
    result = calculate_area(sample_width, sample_height)
    print(result)