class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def find_difference(rect1, rect2):
    return abs(rect1.area() - rect2.area())

if __name__ == '__main__':
    rect1 = Rectangle(5, 3)
    rect2 = Rectangle(4, 6)
    difference = find_difference(rect1, rect2)
    print(difference)