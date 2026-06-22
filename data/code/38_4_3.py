import math

def calculate_cone_volume(r, h):
    return (1/3) * math.pi * r**2 * h

if __name__ == '__main__':
    r = 6
    h = 9
    volume = calculate_cone_volume(r, h)
    print(volume)