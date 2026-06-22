import math

def volume_of_cone(radius, height):
    return (1 / 3) * math.pi * radius ** 2 * height

if __name__ == '__main__':
    result = volume_of_cone(8, 11)
    print(f"{result:.2f}")