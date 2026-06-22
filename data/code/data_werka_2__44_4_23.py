class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    rectangles = [
        Rectangle(5, 3),
        Rectangle(7, 2),
        Rectangle(10, 4)
    ]
    for rect in rectangles:
        perimeter = rect.calculate_perimeter()
        print(perimeter)