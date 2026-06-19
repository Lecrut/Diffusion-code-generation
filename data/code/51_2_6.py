def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    rectangle_dimensions = {
        'rectangle1': {'length': 6, 'width': 4},
        'rectangle2': {'length': 9, 'width': 5}
    }
    
    for name, dimensions in rectangle_dimensions.items():
        length = dimensions['length']
        width = dimensions['width']
        perimeter = calculate_rectangle_perimeter(length, width)
        print(f"Perimeter of {name}: {perimeter}")