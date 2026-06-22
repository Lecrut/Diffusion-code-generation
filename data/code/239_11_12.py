class Rectangle:
    def __init__(self, length=4, width=3):
        self.length = length
        self.width = width
    
    def compute_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(rect.compute_perimeter())