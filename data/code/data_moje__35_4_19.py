def calculate_cube_volume(edge_length):
    return edge_length * edge_length * edge_length

if __name__ == '__main__':
    class VolumeCalculator:
        def __init__(self, length):
            self.length = length

        def get_volume(self):
            return calculate_cube_volume(self.length)

    edge_1 = 2.0
    calc_1 = VolumeCalculator(edge_1)
    print(calc_1.get_volume())

    edge_2 = 4.5
    calc_2 = VolumeCalculator(edge_2)
    print(calc_2.get_volume())

    edge_3 = 0.5
    calc_3 = VolumeCalculator(edge_3)
    print(calc_3.get_volume())