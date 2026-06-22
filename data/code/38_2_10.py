import math

def compute_cone_volume(radius=3, height=7):
    return (1.0 / 3.0) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    volume = compute_cone_volume()
    print(volume)