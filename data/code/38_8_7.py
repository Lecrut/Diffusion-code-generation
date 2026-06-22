import math

def cone_volume(radius, height):
    volume = (1/3) * math.pi * radius**2 * height
    return f"{volume:.2f}"

if __name__ == '__main__':
    result = cone_volume(8, 11)
    print(result)