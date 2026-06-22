def validate_dimensions(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")

def calculate_area(length, width):
    return length * width

def find_difference(area1, area2):
    return abs(area1 - area2)

class Rectangle:
    def __init__(self, length, width):
        validate_dimensions(length, width)
        self.length = length
        self.width = width
    
    def area(self):
        return calculate_area(self.length, self.width)

if __name__ == '__main__':
    try:
        rect1 = Rectangle(9, 2)
        rect2 = Rectangle(6, 3)
        
        area1 = rect1.area()
        area2 = rect2.area()
        
        difference = find_difference(area1, area2)
        
        print(f'Area of rectangle 1: {area1}')
        print(f'Area of rectangle 2: {area2}')
        print(f'Difference in areas: {difference}')
    except ValueError as e:
        print(e)