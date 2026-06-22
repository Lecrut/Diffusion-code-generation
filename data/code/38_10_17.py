import math

def calculate_cone_volume(base_radius: float, cone_height: float) -> float:
    area_of_base = math.pi * (base_radius ** 2)
    volume = area_of_base * cone_height / 3.0
    return volume

if __name__ == '__main__':
    r = 5.0
    h = 10.0
    vol = calculate_cone_volume(r, h)
    print(vol)