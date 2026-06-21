def calculate_area(width: int, height: int) -> int:
    return width * height

if __name__ == '__main__':
    sample_width = 5
    sample_height = 10
    area = calculate_area(sample_width, sample_height)
    print(area)