class Cube:
    VOLUME_EXPONENT = 3

    def __init__(self, edge_length):
        self.edge_length = edge_length

    @staticmethod
    def calculate_volume(edge_length):
        return edge_length ** Cube.VOLUME_EXPONENT

if __name__ == '__main__':
    edge = 4
    result = Cube.calculate_volume(edge)
    print(result)