class Cube:
    def __init__(self, edge_length):
        self.edge_length = edge_length

    def get_volume(self):
        return self._power_function(self.edge_length, 3)

    @staticmethod
    def _power_function(base, exponent):
        result = 1
        for _ in range(exponent):
            result *= base
        return result

if __name__ == '__main__':
    SAMPLE_EDGE = 6
    my_cube = Cube(SAMPLE_EDGE)
    print(my_cube.get_volume())