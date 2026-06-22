def calculate_area(dimensions):
    width = dimensions['width']
    height = dimensions['height']
    return width * height

if __name__ == '__main__':
    dims = {'width': 5, 'height': 3}
    area = calculate_area(dims)
    print(area)