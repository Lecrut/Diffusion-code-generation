class Cone:
    PI = 3.141592653589793

    def __init__(self, radius, height):
        if radius < 0 or height < 0:
            raise ValueError("Dimensions must be non-negative")
        self.radius = radius
        self.height = height

    def volume(self):
        return (1/3) * self.PI * (self.radius ** 2) * self.height

if __name__ == '__main__':
    cone = Cone(radius=5, height=10)
    print(cone.volume())