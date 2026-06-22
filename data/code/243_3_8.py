class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

if __name__ == '__main__':
    circle1 = Circle(10)
    print(circle1.perimeter())