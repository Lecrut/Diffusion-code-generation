def calculate_area_rectangle(width, height):
    return width * height

def calculate_perimeter_rectangle(width, height):
    return 2 * (width + height)

def calculate_area_square(side_length):
    return side_length ** 2

def calculate_perimeter_square(side_length):
    return 4 * side_length

def compare_shapes():
    rectangle_width = 5
    rectangle_height = 3
    square_side_length = 5

    rectangle_area = calculate_area_rectangle(rectangle_width, rectangle_height)
    rectangle_perimeter = calculate_perimeter_rectangle(rectangle_width, rectangle_height)
    square_area = calculate_area_square(square_side_length)
    square_perimeter = calculate_perimeter_square(square_side_length)

    comparison_results = {
        "rectangle": {
            "area": rectangle_area,
            "perimeter": rectangle_perimeter
        },
        "square": {
            "area": square_area,
            "perimeter": square_perimeter
        }
    }

    return comparison_results

if __name__ == '__main__':
    result = compare_shapes()
    print(result)