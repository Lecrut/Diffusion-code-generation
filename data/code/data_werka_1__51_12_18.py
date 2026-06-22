def validate_dimensions(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive numbers.")

class Rectangle:
    def __init__(self, width, height):
        validate_dimensions(width, height)
        self.width = width
        self.height = height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    try:
        rect1 = Rectangle(8, 6)
        perimeter1 = rect1.calculate_perimeter()
        print(perimeter1)
        
        rect2 = Rectangle(4.5, 3.2)
        perimeter2 = rect2.calculate_perimeter()
        print(perimeter2)
    except ValueError as e:
        print(e)