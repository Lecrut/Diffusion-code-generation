def calculate_area_and_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return {'area': area, 'perimeter': perimeter}

def compare_figures():
    rectangle_length = 5
    rectangle_width = 3
    square_side = 5

    rectangle_properties = calculate_area_and_perimeter(rectangle_length, rectangle_width)
    square_properties = calculate_area_and_perimeter(square_side, square_side)

    comparison_results = {
        'rectangle': rectangle_properties,
        'square': square_properties,
        'area_comparison': rectangle_properties['area'] > square_properties['area'],
        'perimeter_comparison': rectangle_properties['perimeter'] > square_properties['perimeter']
    }

    return comparison_results

if __name__ == '__main__':
    results = compare_figures()
    print(results)