import math

def cone_volume(radius=8, height=11):
    volume = (1/3) * math.pi * radius**2 * height
    return f"{volume:.2f}"

if __name__ == '__main__':
    print(cone_volume())