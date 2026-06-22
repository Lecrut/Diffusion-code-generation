class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def create_five():
        return [Rectangle(5, 3) for _ in range(5)]

if __name__ == '__main__':
    rectangles = Rectangle.create_five()
    print([(rect.width, rect.height) for rect in rectangles])