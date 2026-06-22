class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)
    
    def get_perimeter(self):
        return Rectangle.calculate_perimeter(self.length, self.width)

if __name__ == '__main__':
    rect = Rectangle(10, 5)
    perimeter = rect.get_perimeter()
    print(perimeter)