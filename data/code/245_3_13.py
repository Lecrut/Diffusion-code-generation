class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def calculate_area(rectangle):
        return rectangle.width * rectangle.height

    @staticmethod
    def compare_areas(rectangle1, rectangle2):
        area1 = Rectangle.calculate_area(rectangle1)
        area2 = Rectangle.calculate_area(rectangle2)
        return area1 == area2

if __name__ == '__main__':
    rect1 = Rectangle(3.0, 4.0)
    rect2 = Rectangle(5.0, 6.0)
    result1 = Rectangle.compare_areas(rect1, rect2)
    print(f"Rectangle 1 dimensions: {rect1.width}, {rect1.height}")
    print(f"Rectangle 2 dimensions: {rect2.width}, {rect2.height}")
    print(f"Ares of rectangles are equal: {result1}")