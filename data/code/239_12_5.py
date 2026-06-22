class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width
    
    @staticmethod
    def calculate_perimeter(length: float, width: float) -> float:
        return 2 * (length + width)

if __name__ == '__main__':
    rect = Rectangle(10.0, 5.0)
    perimeter = Rectangle.calculate_perimeter(rect.length, rect.width)
    print(perimeter)