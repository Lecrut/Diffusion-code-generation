def compute_cone_volume(radius: float, height: float) -> float:
    import math
    return (1 / 3) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    radius = 5
    height = 10
    volume = compute_cone_volume(radius, height)
    print(volume)