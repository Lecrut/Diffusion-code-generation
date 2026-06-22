def rectangle_area(length: float, width: float) -> float:
    return length * width

if __name__ == '__main__':
    sample_length = 5.0
    sample_width = 10.0
    area = rectangle_area(sample_length, sample_width)
    print(area)