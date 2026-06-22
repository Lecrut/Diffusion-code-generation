class Rectangle:
    WIDTH = 10
    HEIGHT = 20

    @staticmethod
    def create_rectangles():
        return [Rectangle() for _ in range(5)]

if __name__ == '__main__':
    rectangles = Rectangle.create_rectangles()
    print(f"Created {len(rectangles)} rectangles with dimensions {Rectangle.WIDTH}x{Rectangle.HEIGHT}")