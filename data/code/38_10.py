from typing import Union

VolumeType = Union[int, float]

def compute_cone_volume(radius: float, height: float) -> VolumeType:
    pi = 3.141592653589793
    return (1 / 3) * pi * (radius ** 2) * height

if __name__ == '__main__':
    fixed_radius = 5
    fixed_height = 10
    result = compute_cone_volume(fixed_radius, fixed_height)
    print(result)