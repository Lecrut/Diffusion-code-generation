class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2 * 3.141592653589793 * self.radius * (self.radius + self.height)

if __name__ == '__main__':
    cyl = Cylinder(3, 5)
    print(cyl.surface_area())