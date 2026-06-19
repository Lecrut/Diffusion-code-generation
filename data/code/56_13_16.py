def calculate_area_rectangle(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

def calculate_perimeter_rectangle(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return 2 * (length + width)

def calculate_area_square(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be a positive number.")
    return side_length ** 2

def calculate_perimeter_square(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be a positive number.")
    return 4 * side_length

def compare_rectangle_and_square(length, width, side_length):
    rectangle_area = calculate_area_rectangle(length, width)
    rectangle_perimeter = calculate_perimeter_rectangle(length, width)
    square_area = calculate_area_square(side_length)
    square_perimeter = calculate_perimeter_square(side_length)

    comparison_result = {
        "rectangle": {
            "area": rectangle_area,
            "perimeter": rectangle_perimeter
        },
        "square": {
            "area": square_area,
            "perimeter": square_perimeter
        }
    }

    return comparison_result

if __name__ == '__main__':
    length = 8.0
    width = 5.0
    side_length = 5.0
    result = compare_rectangle_and_square(length, width, side_length)
    print(result)