def calculate_area_and_perimeter_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return {'area': area, 'perimeter': perimeter}

def calculate_area_and_perimeter_square(side_length):
    area = side_length ** 2
    perimeter = 4 * side_length
    return {'area': area, 'perimeter': perimeter}

def compare_figures():
    rectangle_dimensions = (5, 3)
    square_side_length = 5

    rectangle_properties = calculate_area_and_perimeter_rectangle(*rectangle_dimensions)
    square_properties = calculate_area_and_perimeter_square(square_side_length)

    comparison_results = {
        'rectangle': rectangle_properties,
        'square': square_properties
    }

    return comparison_results

if __name__ == '__main__':
    results = compare_figures()
    print(results)