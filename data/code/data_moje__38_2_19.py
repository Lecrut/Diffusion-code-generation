import math

def compute_cone_volume(radius, height):
    pi_value = math.pi
    base_area = pi_value * radius * radius
    volume = base_area * height / 3.0
    return volume

if __name__ == '__main__':
    dimensions = {'radius': 3, 'height': 7}
    r = dimensions['radius']
    h = dimensions['height']
    vol = compute_cone_volume(r, h)
    print(vol)