class Rectangle:
    WIDTH = 10
    HEIGHT = 20

    @staticmethod
    def create_five_rectangles():
        return [Rectangle() for _ in range(5)]

if __name__ == '__main__':
    rectangles = Rectangle.create_five_rectangles()
    print(f"Width: {rectangles[0].WIDTH}, Height: {rectangles[0].HEIGHT}")