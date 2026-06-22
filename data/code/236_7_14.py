class Rectangle:
    def __init__(self, width, height):
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise ValueError("Width and height must be numbers.")
        self.width = width
        self.height = height

    @staticmethod
    def create_five_identical():
        return [Rectangle(10, 20) for _ in range(5)]

if __name__ == '__main__':
    rectangles = Rectangle.create_five_identical()
    for rect in rectangles:
        print(f"Width: {rect.width}, Height: {rect.height}")