def calculate_rectangle_area(length, width):
    return length * width

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def calculate_square_area(side_length):
    return side_length ** 2

def calculate_square_perimeter(side_length):
    return 4 * side_length

if __name__ == '__main__':
    rectangle_length = 7.0
    rectangle_width = 3.0
    square_side_length = 5.0

    rectangle_area = calculate_rectangle_area(rectangle_length, rectangle_width)
    rectangle_perimeter = calculate_rectangle_perimeter(rectangle_length, rectangle_width)
    square_area = calculate_square_area(square_side_length)
    square_perimeter = calculate_square_perimeter(square_side_length)

    comparison_results = {
        'rectangle': {
            'area': rectangle_area,
            'perimeter': rectangle_perimeter
        },
        'square': {
            'area': square_area,
            'perimeter': square_perimeter
        }
    }

    print(comparison_results)