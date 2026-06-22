def compute_rectangle_area(width: float, height: float) -> float:
    return width * height
if __name__ == '__main__':
    sample_width = 10.0
    sample_height = 5.0
    area = compute_rectangle_area(sample_width, sample_height)
    print(area)