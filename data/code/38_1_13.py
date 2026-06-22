import math

def calculate_cone_volume(radius, height):
    return (1.0 / 3.0) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    result = calculate_cone_volume(5, 10)
    print(result)