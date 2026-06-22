def calculate_rectangle_area(length, width):
    return length * width

if __name__ == '__main__':
    sample_values = {
        'length': 10,
        'width': 5
    }
    area = calculate_rectangle_area(sample_values['length'], sample_values['width'])
    print(area)