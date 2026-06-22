import math

CONE_PARAMS = {
    "radius": 4,
    "height": 12
}

def get_cone_volume():
    r = CONE_PARAMS["radius"]
    h = CONE_PARAMS["height"]
    return math.pi * r * r * h / 3.0

if __name__ == '__main__':
    print(get_cone_volume())