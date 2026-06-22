class Shape:
    def __init__(self, side_length):
        self.side_length = side_length

    @staticmethod
    def area_rectangle(length, width):
        return length * width

    @staticmethod
    def perimeter_rectangle(length, width):
        return 2 * (length + width)

    @staticmethod
    def area_square(side_length):
        return side_length ** 2

    @staticmethod
    def perimeter_square(side_length):
        return 4 * side_length

def compare_shapes():
    rectangle_length = 5
    rectangle_width = 3
    square_side = 5

    rectangle_area = Shape.area_rectangle(rectangle_length, rectangle_width)
    rectangle_perimeter = Shape.perimeter_rectangle(rectangle_length, rectangle_width)

    square_area = Shape.area_square(square_side)
    square_perimeter = Shape.perimeter_square(square_side)

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
    results = compare_shapes()
    print(results)