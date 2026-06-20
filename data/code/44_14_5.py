class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_perimeter(self):
        return (self.width + self.height) * 2

if __name__ == '__main__':
    width = 5
    height = 3
    rect = Rectangle(width, height)
    print(rect.get_perimeter())