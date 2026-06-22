def calculate_area(length, width):
    return length * width

if __name__ == '__main__':
    sample_dimensions = {'length': 5, 'width': 3}
    area = calculate_area(sample_dimensions['length'], sample_dimensions['width'])
    print(area)