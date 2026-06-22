class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def create_five_identical():
        return [Rectangle(5, 10) for _ in range(5)]

if __name__ == '__main__':
    rectangles = Rectangle.create_five_identical()
    print(rectangles)