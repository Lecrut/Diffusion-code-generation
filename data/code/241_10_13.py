AREA_CONSTANT = 1.0

def calculate_area(width: float, height: float) -> float:
    return width * height * AREA_CONSTANT
if __name__ == '__main__':
    sample_width = 8.0
    sample_height = 3.0
    result = calculate_area(sample_width, sample_height)
    print(result)