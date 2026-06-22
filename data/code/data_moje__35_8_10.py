class Cube:
    def __init__(self, edge):
        self.edge = edge

    def volume(self):
        return self.edge * self.edge * self.edge

if __name__ == '__main__':
    my_cube = Cube(10)
    print(my_cube.volume())