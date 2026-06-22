import math

class Cone:
    def __init__(self, radius, height):
        if radius <= 0 or height <= 0:
            raise ValueError("Radius and height must be positive")
        self.radius = radius
        self.height = height

    def volume(self):
        return (1 / 3) * math.pi * (self.radius ** 2) * self.height

def main():
    cone = Cone(8, 11)
    vol = cone.volume()
    print(f"{vol:.2f}")

if __name__ == '__main__':
    main()