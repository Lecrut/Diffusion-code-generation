class Rectangle:
    def __init__(self, length, width):
        if not all(isinstance(d, (int, float)) and d > 0 for d in [length, width]):
            raise ValueError("All dimensions must be positive numbers.")
        self.length = length
        self.width = width

    @staticmethod
    def perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(f"Perimeter: {Rectangle.perimeter(rect.length, rect.width)}")