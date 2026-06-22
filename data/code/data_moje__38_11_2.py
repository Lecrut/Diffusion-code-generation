import math

def calculate_cone_volume(radius, height):
    return (1/3) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    base_radius = 5
    cone_height = 10
    volume = calculate_cone_volume(base_radius, cone_height)
    print(volume)