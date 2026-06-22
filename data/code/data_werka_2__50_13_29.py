class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def calculate_difference(rect1, rect2):
    return abs(rect1.area() - rect2.area())

if __name__ == '__main__':
    LENGTH_1 = 10
    WIDTH_1 = 5
    LENGTH_2 = 8
    WIDTH_2 = 3

    rect1 = Rectangle(LENGTH_1, WIDTH_1)
    rect2 = Rectangle(LENGTH_2, WIDTH_2)

    difference = calculate_difference(rect1, rect2)
    print(difference)