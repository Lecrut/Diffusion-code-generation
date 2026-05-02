class GeometryUtils:
    @staticmethod
    def calculate_rectangle_perimeter(length, width):
        return 2 * (length + width)
if __name__ == '__main__':
    length_val = 10
    width_val = 5
    perimeter = GeometryUtils.calculate_rectangle_perimeter(length_val, width_val)
    print(perimeter)