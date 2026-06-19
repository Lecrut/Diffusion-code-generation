def calculate_area(length, width=None):
    if width is None:
        return length ** 2
    else:
        return length * width

def calculate_perimeter(length, width=None):
    if width is None:
        return 4 * length
    else:
        return 2 * (length + width)

if __name__ == '__main__':
    side_length = 5
    rectangle_length = 5
    rectangle_width = 3

    square_area = calculate_area(side_length)
    square_perimeter = calculate_perimeter(side_length)

    rectangle_area = calculate_area(rectangle_length, rectangle_width)
    rectangle_perimeter = calculate_perimeter(rectangle_length, rectangle_width)

    comparison_results = {
        'Square': {
            'Area': square_area,
            'Perimeter': square_perimeter
        },
        'Rectangle': {
            'Area': rectangle_area,
            'Perimeter': rectangle_perimeter
        }
    }

    print(comparison_results)