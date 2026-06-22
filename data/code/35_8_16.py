class CubeCalculator:
    def __init__(self, edge_length):
        self.edge_length = edge_length

    def compute_volume(self):
        return self.edge_length ** 3

    def compute_surface_area(self):
        return 6 * (self.edge_length ** 2)

if __name__ == '__main__':
    calculator = CubeCalculator(6)
    print(calculator.compute_volume())
    print(calculator.compute_surface_area())