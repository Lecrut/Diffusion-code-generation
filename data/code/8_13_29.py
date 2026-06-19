import math

class ShapeScaler:
    def __init__(self, scale_factor):
        self.scale_factor = scale_factor

    def scaled_area_rectangle(self, length, width):
        return (length * width) * (self.scale_factor ** 2)

    def scaled_area_circle(self, radius):
        return (math.pi * (radius ** 2)) * (self.scale_factor ** 2)

if __name__ == '__main__':
    scaler = ShapeScaler(1.5)
    print(scaler.scaled_area_rectangle(4, 5))
    print(scaler.scaled_area_circle(3))