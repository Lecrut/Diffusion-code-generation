AREA_CONSTANT = 1

def calculate_rectangle_area(width: float, height: float) -> float:
    return (width * AREA_CONSTANT) * height

if __name__ == '__main__':
    sample_width = 12
    sample_height = 9
    print(calculate_rectangle_area(sample_width, sample_height))