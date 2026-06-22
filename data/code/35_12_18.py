class CubeVolumeCalculator:
    def __init__(self, edge_length):
        self.edge_length = edge_length
        self._volume = None

    def compute_volume(self):
        self._volume = self.edge_length ** 3
        return self._volume

    def get_edge_length(self):
        return self.edge_length

    def get_computed_volume(self):
        if self._volume is None:
            self.compute_volume()
        return self._volume

if __name__ == '__main__':
    calculator = CubeVolumeCalculator(6)
    print(calculator.compute_volume())
    print(calculator.get_edge_length())
    print(calculator.get_computed_volume())