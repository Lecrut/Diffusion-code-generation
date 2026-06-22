import math

def volume_of_cone(r, h):
    if r <= 0 or h <= 0:
        return 0.0
    return (math.pi * r * r * h) / 3

if __name__ == '__main__':
    radius_val = 6.5
    height_val = 14.2
    final_volume = volume_of_cone(radius_val, height_val)
    print(final_volume)