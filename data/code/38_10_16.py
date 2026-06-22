import math

def compute_cone_volume(radius: float, height: float) -> float:
    return (1/3) * math.pi * (radius ** 2) * height

if __name__ == "__main__":
    r: float = 5
    h: float = 10
    volume: float = compute_cone_volume(r, h)
    print(volume)