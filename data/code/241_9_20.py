def calculate_area(length, width):
    return length * width

if __name__ == '__main__':
    dimensions = {'length': 5, 'width': 3}
    area = calculate_area(dimensions['length'], dimensions['width'])
    print(area)