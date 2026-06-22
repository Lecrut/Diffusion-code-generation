class Rectangle:
    def __init__(self, width=5, height=3):
        self.width = width
        self.height = height
    
    @staticmethod
    def calculate_perimeter(width, height):
        return 2 * (width + height)

if __name__ == '__main__':
    rect = Rectangle()
    perimeter_result = Rectangle.calculate_perimeter(rect.width, rect.height)
    print(perimeter_result)