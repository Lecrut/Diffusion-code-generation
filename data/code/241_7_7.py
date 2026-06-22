class Rectangle:
    @staticmethod
    def validate_dimensions(length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
    
    @staticmethod
    def area():
        length = 5
        width = 3
        Rectangle.validate_dimensions(length, width)
        return length * width

if __name__ == '__main__':
    print(Rectangle.area())