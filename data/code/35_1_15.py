class CubeCalculator:
    @staticmethod
    def get_volume(edge_length):
        return CubeCalculator._calculate_power(edge_length)

    @staticmethod
    def _calculate_power(value):
        return value * value * value

if __name__ == '__main__':
    test_edge = 7
    final_volume = CubeCalculator.get_volume(test_edge)
    print(final_volume)