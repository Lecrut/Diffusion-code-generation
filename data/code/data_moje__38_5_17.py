from math import pi

def compute_cone_volume(radius: float, height: float) -> float:
    return (pi * radius * radius * height) / 3.0

if __name__ == '__main__':
    radius: float = 2.5
    height: float = 4.0
    volume: float = compute_cone_volume(radius, height)
    print(volume)