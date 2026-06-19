class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    rectangles = [
        Rectangle(10, 5),
        Rectangle(7, 3),
        Rectangle(4.5, 6.2)
    ]

    for rect in rectangles:
        perimeter = Rectangle.calculate_perimeter(rect.length, rect.width)
        print(f"The perimeter of a rectangle with length {rect.length} and width {rect.width} is: {perimeter}")