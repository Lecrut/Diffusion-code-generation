class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    dimensions = {'length': 10, 'width': 5}
    rect = Rectangle(dimensions['length'], dimensions['width'])
    area_result = rect.area()
    print(area_result)