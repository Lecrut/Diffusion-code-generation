PERIMETER_FACTOR = 2

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_perimeter(self):
        return PERIMETER_FACTOR * (self.length + self.width)

def validate_dimensions(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise ValueError("Length and width must be numbers.")
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive.")

if __name__ == '__main__':
    try:
        rect1 = Rectangle(8, 5)
        perimeter1 = rect1.calculate_perimeter()
        print(perimeter1)
        
        rect2 = Rectangle(12, 7)
        perimeter2 = rect2.calculate_perimeter()
        print(perimeter2)
    except ValueError as e:
        print(e)