def calculate_area(width: float, height: float) -> float:
    area = width * height
    return area

if __name__ == '__main__':
    sample_width = 7.5
    sample_height = 2.8
    result = calculate_area(sample_width, sample_height)
    print(result)