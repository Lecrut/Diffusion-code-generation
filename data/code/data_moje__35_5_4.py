class CubeVolumeCalculator:
    DEFAULT_EDGE = 6.0

    @staticmethod
    def _validate_edge(edge):
        if edge <= 0:
            raise ValueError("Edge length must be positive")
        return edge

    @staticmethod
    def calculate(edge_length):
        valid_edge = CubeVolumeCalculator._validate_edge(edge_length)
        return valid_edge * valid_edge * valid_edge

if __name__ == '__main__':
    edge = CubeVolumeCalculator.DEFAULT_EDGE
    result = CubeVolumeCalculator.calculate(edge)
    print(result)