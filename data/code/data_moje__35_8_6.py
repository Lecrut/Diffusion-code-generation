class Cube:
    EDGE_POWER = 3

    @staticmethod
    def compute_volume(edge_length):
        return edge_length ** Cube.EDGE_POWER

if __name__ == '__main__':
    sample_edge_length = 6
    computed_value = Cube.compute_volume(sample_edge_length)
    print(computed_value)