import math

PI = math.pi

CONSTANTS = {
    "r": 6,
    "h": 9
}

def compute_cone_volume(radius, height):
    return (1 / 3) * PI * radius ** 2 * height

if __name__ == '__main__':
    sample_radius = CONSTANTS["r"]
    sample_height = CONSTANTS["h"]
    calculated_volume = compute_cone_volume(sample_radius, sample_height)
    print(calculated_volume)