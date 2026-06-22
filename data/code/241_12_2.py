def calculate_area(length, width):
    return length * width

if __name__ == '__main__':
    dimensions = {'length': 10, 'width': 5}
    area_result = calculate_area(dimensions['length'], dimensions['width'])
    print(area_result)