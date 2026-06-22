class Cube:
    def __init__(self, edge_length):
        self.edge_length = edge_length

    def volume(self):
        return self.edge_length ** 3

    def surface_area(self):
        return 6 * (self.edge_length ** 2)

if __name__ == '__main__':
    test_edge = 4.5
    cube_instance = Cube(test_edge)
    print(cube_instance.volume())
    print(cube_instance.surface_area())