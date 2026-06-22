def compute_rectangle_area(width, height):
    return width * height

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def area(self):
        return compute_rectangle_area(self.width, self.height)

if __name__ == '__main__':
    rect = Rectangle(12, 7)
    print(compute_rectangle_area(rect.get_width(), rect.get_height()))
    print(rect.area())