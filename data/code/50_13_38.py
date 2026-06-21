class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def calculate_difference(rect1, rect2):
    return abs(rect1.area() - rect2.area())

if __name__ == '__main__':
    rectangles = {
        'rect1': {'length': 8, 'width': 5},
        'rect2': {'length': 6, 'width': 7}
    }
    
    rect1 = Rectangle(rectangles['rect1']['length'], rectangles['rect1']['width'])
    rect2 = Rectangle(rectangles['rect2']['length'], rectangles['rect2']['width'])
    
    difference = calculate_difference(rect1, rect2)
    print(difference)