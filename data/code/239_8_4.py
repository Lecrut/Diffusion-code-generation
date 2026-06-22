class Rectangle:
    def __init__(self, width=5, height=3):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    rect = Rectangle()
    print(rect.calculate_perimeter())