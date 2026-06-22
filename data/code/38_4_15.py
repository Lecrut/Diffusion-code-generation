import math

def get_cone_volume(r, h):
    return (1 / 3) * math.pi * (r * r) * h

if __name__ == '__main__':
    params = {'radius': 6, 'height': 9}
    r = params['radius']
    h = params['height']
    v = get_cone_volume(r, h)
    print(v)