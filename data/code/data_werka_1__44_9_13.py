class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def calculate_perimeter(length, width):
        if not all(isinstance(x, (int, float)) for x in [length, width]):
            raise TypeError("Both dimensions must be numeric.")
        if length <= 0 or width <= 0:
            raise ValueError("Dimensions must be positive numbers.")
        return 2 * (length + width)

if __name__ == '__main__':
    try:
        length = 15
        width = 7
        rectangle = Rectangle(length, width)
        perimeter = Rectangle.calculate_perimeter(length, width)
        print(f"Length: {rectangle.length}")
        print(f"Width: {rectangle.width}")
        print(f"Perimeter: {perimeter}")
    except (ValueError, TypeError) as e:
        print(e)