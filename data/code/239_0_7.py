def calculate_perimeter(width, height):
    return 2 * (width + height)

dimensions = {'width': 5, 'height': 3}

if __name__ == '__main__':
    perimeter = calculate_perimeter(dimensions['width'], dimensions['height'])
    print(perimeter)