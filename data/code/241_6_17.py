class Rectangle:
    LENGTH = 10
    WIDTH = 5

    @staticmethod
    def calculate_area():
        return Rectangle.LENGTH * Rectangle.WIDTH

if __name__ == '__main__':
    area = Rectangle.calculate_area()
    print(area)