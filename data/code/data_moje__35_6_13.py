class CubeCalculator:
    EXPONENT = 3

    @staticmethod
    def calculate_volume(edge_length):
        return edge_length ** CubeCalculator.EXPONENT

if __name__ == '__main__':
    side = 4.0
    vol = CubeCalculator.calculate_volume(side)
    print(vol)