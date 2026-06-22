class Rectangle:
    def __init__(self, length, width):
        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
            raise ValueError("Length and width must be numbers")
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive")
        self.length = length
        self.width = width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    rect1 = Rectangle(10, 5)
    perimeter1 = rect1.calculate_perimeter()
    print(f"Perimeter of rectangle 1: {perimeter1}")
    
    rect2 = Rectangle(7, 3)
    perimeter2 = rect2.calculate_perimeter()
    print(f"Perimeter of rectangle 2: {perimeter2}")