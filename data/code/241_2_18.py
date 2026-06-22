class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def compute_area(self):
        return self.length * self.width

if __name__ == '__main__':
    rectangles = {
        'rect1': (10, 5),
        'rect2': (7, 3)
    }
    
    for name, dimensions in rectangles.items():
        rect = Rectangle(*dimensions)
        area = rect.compute_area()
        print(f'{name} area: {area}')