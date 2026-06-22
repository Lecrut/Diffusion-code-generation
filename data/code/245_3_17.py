class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def compare_areas(rect1, rect2):
    return rect1.area() == rect2.area()

if __name__ == '__main__':
    rect1 = Rectangle(3.0, 4.0)
    rect2 = Rectangle(6.0, 2.0)
    rect3 = Rectangle(5.0, 5.0)

    print(f"Rectangle 1 dimensions: {rect1.width}, {rect1.height}")
    print(f"Rectangle 2 dimensions: {rect2.width}, {rect2.height}")
    print(f"Rectangle 3 dimensions: {rect3.width}, {rect3.height}")

    result1 = compare_areas(rect1, rect2)
    print(f"Area of Rectangle 1 vs Rectangle 2 are equal: {result1}")

    result2 = compare_areas(rect1, rect3)
    print(f"Area of Rectangle 1 vs Rectangle 3 are equal: {result2}")