class PyramidTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def print_vertices(self):
        x_coords = [0, self.base, 0]
        y_coords = [0, 0, self.height]
        for i in range(3):
            print(f"Vertex {i}: ({x_coords[i]}, {y_coords[i]})")

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle = PyramidTriangle(base=5, height=4)
    triangle.print_vertices()
    print(f"Area: {triangle.calculate_area()}")