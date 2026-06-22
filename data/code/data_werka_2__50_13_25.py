class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def find_difference(rect1, rect2):
    return abs(rect1.area() - rect2.area())

if __name__ == '__main__':
    config = {
        'rect1': {'length': 8, 'width': 3},
        'rect2': {'length': 5, 'width': 7}
    }
    
    rect1 = Rectangle(config['rect1']['length'], config['rect1']['width'])
    rect2 = Rectangle(config['rect2']['length'], config['rect2']['width'])
    
    difference = find_difference(rect1, rect2)
    print(difference)