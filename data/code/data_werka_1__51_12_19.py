def calculate_perimeter(width, height):
    return 2 * (width + height)

if __name__ == '__main__':
    dimensions = {'width': 8, 'height': 12}
    width = dimensions['width']
    height = dimensions['height']
    perimeter = calculate_perimeter(width, height)
    print(perimeter)