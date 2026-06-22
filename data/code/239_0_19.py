def calculate_perimeter(dimensions):
    width = dimensions['width']
    height = dimensions['height']
    return 2 * (width + height)

if __name__ == '__main__':
    dimensions = {'width': 5, 'height': 3}
    perimeter = calculate_perimeter(dimensions)
    print(perimeter)