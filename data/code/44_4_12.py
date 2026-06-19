class Rectangle:
    DEFAULT_LENGTH = 10
    DEFAULT_WIDTH = 5

    @staticmethod
    def calculate_perimeter(length, width):
        perimeter = 2 * (length + width)
        return perimeter

if __name__ == '__main__':
    rectangles = [
        {"length": 10, "width": 5},
        {"length": 7, "width": 3},
        {"length": 15, "width": 8}
    ]

    for rect in rectangles:
        length = rect.get("length", Rectangle.DEFAULT_LENGTH)
        width = rect.get("width", Rectangle.DEFAULT_WIDTH)
        perimeter = Rectangle.calculate_perimeter(length, width)
        print(f"The perimeter of a rectangle with length {length} and width {width} is: {perimeter}")