class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return 3.14159 * self.radius ** 2
if __name__ == '__main__':
    my_circle = Circle(5)
    area = my_circle.calculate_area()
    print(area)