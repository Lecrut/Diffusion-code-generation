class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def find_difference(rect1, rect2):
    return abs(rect1.area() - rect2.area())
if __name__ == '__main__':
    rect1 = Rectangle(9, 3)
    rect2 = Rectangle(6, 7)
    area1 = rect1.area()
    area2 = rect2.area()
    difference = find_difference(rect1, rect2)
    print(f'Area of rectangle 1: {area1}')
    print(f'Area of rectangle 2: {area2}')
    print(f'Difference in areas: {difference}')