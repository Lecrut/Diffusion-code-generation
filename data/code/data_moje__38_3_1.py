import math

def calculate_cone_volume(radius, height):
    return (math.pi * radius ** 2 * height) / 3

if __name__ == '__main__':
    result = calculate_cone_volume(4, 12)
    print(result)