def calculate_area(length, width):
    return length * width

if __name__ == '__main__':
    sample_values = {
        'length': 5,
        'width': 3
    }
    area = calculate_area(sample_values['length'], sample_values['width'])
    print(area)