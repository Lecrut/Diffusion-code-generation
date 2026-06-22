class Rectangle:
    LENGTH = 10
    WIDTH = 5

    @staticmethod
    def calculate_area(length, width):
        return length * width

if __name__ == '__main__':
    area = Rectangle.calculate_area(Rectangle.LENGTH, Rectangle.WIDTH)
    print(area)