class Rectangle:
    LENGTH = 5
    WIDTH = 3

    @staticmethod
    def calculate_area():
        return Rectangle.LENGTH * Rectangle.WIDTH

if __name__ == '__main__':
    print(Rectangle.calculate_area())