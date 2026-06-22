class Geometry:
    PERIMETER_CONSTANT = 2

    @staticmethod
    def calculate_rectangle_perimeter(length, width):
        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
            raise ValueError("Length and width must be numeric values.")
        return Geometry.PERIMETER_CONSTANT * (length + width)

if __name__ == '__main__':
    length = 7
    width = 4
    try:
        perimeter = Geometry.calculate_rectangle_perimeter(length, width)
        print(f"The perimeter of the rectangle with length {length} and width {width} is: {perimeter}")
    except ValueError as e:
        print(e)