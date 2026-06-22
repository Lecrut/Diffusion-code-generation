def calculate_rectangle_perimeter(width, height):
    return 2 * (width + height)

if __name__ == '__main__':
    dimensions = {
        'sample1': {'width': 5, 'height': 3},
        'sample2': {'width': 7, 'height': 4},
        'sample3': {'width': 10, 'height': 6}
    }
    
    for name, size in dimensions.items():
        perimeter = calculate_rectangle_perimeter(size['width'], size['height'])
        print(f"Perimeter of {name} rectangle: {perimeter}")