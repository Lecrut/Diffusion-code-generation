def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    rectangle_properties = {
        'length': 15,
        'width': 8
    }
    perimeter = calculate_perimeter(rectangle_properties['length'], rectangle_properties['width'])
    print(perimeter)