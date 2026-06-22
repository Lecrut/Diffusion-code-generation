def calculate_area(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    return length * width

if __name__ == '__main__':
    area_result = calculate_area(10, 5)
    print(area_result)