def compute_rectangle_area(width, height):
    return float(width * height)

if __name__ == '__main__':
    sample_width = 5.5
    sample_height = 3.2
    area = compute_rectangle_area(sample_width, sample_height)
    print(area)