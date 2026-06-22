class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def create_five_rectangles():
        return [Rectangle(2, 3) for _ in range(5)]

if __name__ == '__main__':
    rectangles = Rectangle.create_five_rectangles()
    print(rectangles)