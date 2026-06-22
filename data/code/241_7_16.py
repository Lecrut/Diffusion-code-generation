class Rectangle:
    @staticmethod
    def area():
        length = 5
        width = 3
        if length > 0 and width > 0:
            return length * width
        else:
            raise ValueError("Length and width must be positive numbers")

if __name__ == '__main__':
    print(Rectangle.area())