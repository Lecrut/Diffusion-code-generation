class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def calculate_area(length, width):
        return length * width

def find_difference(rect1, rect2):
    area1 = Rectangle.calculate_area(rect1.length, rect1.width)
    area2 = Rectangle.calculate_area(rect2.length, rect2.width)
    return abs(area1 - area2)

if __name__ == '__main__':
    rect1 = Rectangle(10, 5)
    rect2 = Rectangle(8, 3)
    difference = find_difference(rect1, rect2)
    print(difference)