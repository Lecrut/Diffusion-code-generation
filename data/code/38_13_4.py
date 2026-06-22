import math

def calculate_cone_volume(radius, height):
    return (math.pi * radius * radius * height) / 3

if __name__ == '__main__':
    r = 5
    h = 10
    result = calculate_cone_volume(r, h)
    print(result)