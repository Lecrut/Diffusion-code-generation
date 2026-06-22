class Rectangle:
    def __init__(self, length, width):
        if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
            raise TypeError("Both dimensions must be numbers.")
        if length <= 0 or width <= 0:
            raise ValueError("Both dimensions must be positive numbers.")
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    try:
        sample_rectangle = Rectangle(15, 8)
        print(sample_rectangle.calculate_perimeter())
        
        another_rectangle = Rectangle(7, 3)
        print(another_rectangle.calculate_perimeter())
    except Exception as e:
        print(e)