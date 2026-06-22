class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    
    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"

def create_rectangle(length, width):
    return Rectangle(length, width)

if __name__ == '__main__':
    rect1 = create_rectangle(6, 4)
    print(rect1)
    perimeter1 = rect1.calculate_perimeter()
    print(perimeter1)
    
    rect2 = create_rectangle(9, 3)
    print(rect2)
    perimeter2 = rect2.calculate_perimeter()
    print(perimeter2)