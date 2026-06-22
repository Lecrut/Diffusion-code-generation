class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def compute_area(self):
        return self.length * self.width

if __name__ == '__main__':
    rect = Rectangle(12, 4)
    area_result = rect.compute_area()
    print(area_result)