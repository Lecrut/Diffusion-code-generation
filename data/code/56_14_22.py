import math

class VolumeCalculator:
    @staticmethod
    def cube_volume(edge_length):
        return edge_length ** 3

    @staticmethod
    def sphere_volume(radius):
        return (4/3) * math.pi * (radius ** 3)

def is_cube_volume_greater(cube_edge, sphere_radius):
    cube_vol = VolumeCalculator.cube_volume(cube_edge)
    sphere_vol = VolumeCalculator.sphere_volume(sphere_radius)
    return cube_vol > sphere_vol

if __name__ == '__main__':
    edge_length = 3
    radius = 2
    result = is_cube_volume_greater(edge_length, radius)
    print(result)