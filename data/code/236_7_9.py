class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def create_five_rectangles():
        return [Rectangle(10, 20) for _ in range(5)]

if __name__ == '__main__':
    rectangles = Rectangle.create_five_rectangles()
    print(f"Number of rectangles created: {len(rectangles)}")