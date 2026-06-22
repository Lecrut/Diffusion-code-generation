class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    rect1 = Rectangle(10, 5)
    perimeter1 = rect1.calculate_perimeter(rect1.length, rect1.width)
    print(f"Perimeter of rectangle 1: {perimeter1}")
    
    rect2 = Rectangle(7, 3)
    perimeter2 = Rectangle.calculate_perimeter(rect2.length, rect2.width)
    print(f"Perimeter of rectangle 2: {perimeter2}")