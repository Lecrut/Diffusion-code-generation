class Rectangle:
    def __init__(self, width=4, height=3):
        self.width = width
        self.height = height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    rect1 = Rectangle(5, 2)
    print(rect1.compute_perimeter())

    rect2 = Rectangle()
    print(rect2.compute_perimeter())