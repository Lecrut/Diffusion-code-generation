class Rectangle:
    @staticmethod
    def calculate_area(length, width):
        return length * width

if __name__ == '__main__':
    rectangle_length = 5
    rectangle_width = 3
    area = Rectangle.calculate_area(rectangle_length, rectangle_width)
    print(area)