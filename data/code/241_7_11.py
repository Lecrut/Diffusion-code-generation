class Rectangle:
    LENGTH = 5
    WIDTH = 3

    @staticmethod
    def area():
        return Rectangle.LENGTH * Rectangle.WIDTH

if __name__ == '__main__':
    print(Rectangle.area())