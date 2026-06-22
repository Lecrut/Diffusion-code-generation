class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        width_value = self.width
        height_value = self.height
        return width_value * height_value

if __name__ == '__main__':
    rect_width = 7.5
    rect_height = 12.0
    rectangle = Rectangle(rect_width, rect_height)
    area_value = rectangle.get_area()
    print(area_value)