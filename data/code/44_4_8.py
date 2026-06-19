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
        Rectangle(15, 8)
    ]

    for rect in rectangles:
        if rect.length > 0 and rect.width > 0:
            perimeter = Rectangle.calculate_perimeter(rect.length, rect.width)
            print(f"The perimeter of a rectangle with length {rect.length} and width {rect.width} is: {perimeter}")
        else:
            print("Invalid input: Length and width must be positive numbers.")