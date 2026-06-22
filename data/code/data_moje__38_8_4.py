import math

PI = math.pi

def calculate_cone_volume(r, h):
    base_area = PI * r * r
    return (base_area * h) / 3

class GeometrySolver:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_volume(self):
        return calculate_cone_volume(self.radius, self.height)

    def get_radius(self):
        return self.radius

if __name__ == '__main__':
    solver = GeometrySolver(8, 11)
    volume = solver.get_volume()
    radius_val = solver.get_radius()
    print(f"{volume:.2f}")