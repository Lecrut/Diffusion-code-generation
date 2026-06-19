class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @staticmethod
    def calculate_area(base, height):
        return base * height

if __name__ == '__main__':
    rectangle_base = 6.3
    rectangle_height = 4.7
    area_result = Rectangle.calculate_area(rectangle_base, rectangle_height)
    print(area_result)