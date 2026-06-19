import math

class ShapeScaler:
    def __init__(self, scale_factor):
        self.scale_factor = scale_factor

    def scaled_area_rectangle(self, length, width):
        area = length * width
        return area * self.scale_factor

    def scaled_area_circle(self, radius):
        area = math.pi * (radius ** 2)
        return area * self.scale_factor

if __name__ == '__main__':
    scaler = ShapeScaler(1.5)
    print(scaler.scaled_area_rectangle(4, 3))
    print(scaler.scaled_area_circle(2))