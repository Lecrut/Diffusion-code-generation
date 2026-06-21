def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers")
    return length * width

if __name__ == '__main__':
    dimensions = {
        'length': 8.0,
        'width': 2.5
    }
    area_result = calculate_area(dimensions['length'], dimensions['width'])
    print(area_result)