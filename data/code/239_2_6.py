class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    rect1_length = 10
    rect1_width = 5
    perimeter1 = Rectangle.calculate_perimeter(rect1_length, rect1_width)
    print(f"Perimeter of rectangle 1: {perimeter1}")