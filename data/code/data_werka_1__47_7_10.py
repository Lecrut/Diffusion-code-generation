def calculate_area(length, width):
    return length * width

if __name__ == '__main__':
    dimensions = (9, 4)
    length, width = dimensions
    area = calculate_area(length, width)
    print(area)