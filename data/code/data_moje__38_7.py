import math

def calculate_cone_volume(radius, height):
    return (math.pi * radius**2 * height) / 3

if __name__ == '__main__':
    radius = 7
    height = 5
    volume = calculate_cone_volume(radius, height)
    print(volume)