class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def find_difference(rect1, rect2):
    return abs(rect1.area() - rect2.area())

if __name__ == '__main__':
    dimensions = {
        'rectangle1': {'length': 5, 'width': 3},
        'rectangle2': {'length': 4, 'width': 6}
    }

    rect1 = Rectangle(dimensions['rectangle1']['length'], dimensions['rectangle1']['width'])
    rect2 = Rectangle(dimensions['rectangle2']['length'], dimensions['rectangle2']['width'])

    difference = find_difference(rect1, rect2)
    print(difference)