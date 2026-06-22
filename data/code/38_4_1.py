import math

def calculate_cone_volume(radius, height):
    return (1/3) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    dimensions = {'radius': 6, 'height': 9}
    result = calculate_cone_volume(dimensions['radius'], dimensions['height'])
    print(result)