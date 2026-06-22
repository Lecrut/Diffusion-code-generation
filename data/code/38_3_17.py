def volume_of_cone(radius, height):
    import math
    return (1 / 3) * math.pi * radius ** 2 * height

if __name__ == '__main__':
    print(volume_of_cone(4, 12))