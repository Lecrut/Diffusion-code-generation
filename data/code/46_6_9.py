class GeometryUtils:
    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    length = 5
    width = 3
    perimeter = GeometryUtils.calculate_perimeter(length, width)
    print(perimeter)