def compute_area(length, width):
    return length * width

if __name__ == '__main__':
    sample_length = 7
    sample_width = 4
    area_result = compute_area(sample_length, sample_width)
    print(f"The area of a rectangle with length {sample_length} and width {sample_width} is {area_result}")