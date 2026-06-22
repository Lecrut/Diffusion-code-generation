class CubeGeometry:
    PI_APPROX = 3.14159
    DEFAULT_EDGE = 6.0

    def __init__(self, edge_length):
        self.edge = float(edge_length)

    def calculate_volume(self):
        return self.edge * self.edge * self.edge

    def calculate_surface_area(self):
        return 6 * self.edge * self.edge

    def calculate_space_diagonal(self):
        return self.edge * 1.73205

if __name__ == '__main__':
    cube = CubeGeometry(4.0)
    vol = cube.calculate_volume()
    area = cube.calculate_surface_area()
    diag = cube.calculate_space_diagonal()
    print(vol)
    print(area)
    print(diag)