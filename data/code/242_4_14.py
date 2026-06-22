import numpy as np

class Polygon:
    def __init__(self, vertices):
        self.vertices = np.array(vertices)

    def area(self):
        n = len(self.vertices)
        area = 0.5 * np.abs(np.dot(self.vertices[:, 0], np.roll(self.vertices[:, 1], 1)) - 
                            np.dot(self.vertices[:, 1], np.roll(self.vertices[:, 0], 1)))
        return area

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return np.pi * self.radius ** 2

if __name__ == '__main__':
    polygon = Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
    circle = Circle(1.5)

    print(f"Polygon area: {polygon.area()}")
    print(f"Circle area: {circle.area()}")

    if polygon.area() > circle.area():
        print("Polygon area is greater than circle area")
    elif polygon.area() < circle.area():
        print("Polygon area is less than circle area")
    else:
        print("Areas are equal")