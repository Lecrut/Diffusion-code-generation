class GeometryHelper:
    @staticmethod
    def calculate_rectangle_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    rectangle_length = 6
    rectangle_width = 4
    perimeter = GeometryHelper.calculate_rectangle_perimeter(rectangle_length, rectangle_width)
    print(perimeter)