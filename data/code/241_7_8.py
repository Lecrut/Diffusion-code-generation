class Rectangle:
    @staticmethod
    def area():
        length = 5
        width = 3
        return length * width

if __name__ == '__main__':
    result = Rectangle.area()
    print(result)