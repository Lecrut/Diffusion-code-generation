class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def compute_surface_area(self):
        return 2 * 3.141592653589793 * self.radius * (self.radius + self.height)

if __name__ == '__main__':
    radius = 5
    height = 10
    cylinder = Cylinder(radius, height)
    print(cylinder.compute_surface_area())