class CubeVolumeCalculator:
    EDGE_POWER = 3

    @staticmethod
    def from_edge_length(edge_length):
        return edge_length ** CubeVolumeCalculator.EDGE_POWER

if __name__ == '__main__':
    edge = 4
    result = CubeVolumeCalculator.from_edge_length(edge)
    print(result)