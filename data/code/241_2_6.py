class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

if __name__ == '__main__':
    rect1 = Rectangle(10, 5)
    area1 = rect1.compute_area()
    print(area1)

    rect2 = Rectangle(7, 3)
    area2 = rect2.compute_area()
    print(area2)