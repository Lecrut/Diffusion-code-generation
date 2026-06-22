class Rectangle:
    @staticmethod
    def calculate_area(length, width):
        return length * width

if __name__ == '__main__':
    area = Rectangle.calculate_area(10.5, 5.0)
    print(area)