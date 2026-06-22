import math

class ShapeScaler:
    def __init__(self, scale_factor):
        self.scale_factor = scale_factor

    def scaled_area_rectangle(self, width, height):
        area = width * height
        return area * (self.scale_factor ** 2)

    def scaled_area_circle(self, radius):
        area = math.pi * (radius ** 2)
        return area * (self.scale_factor ** 2)

if __name__ == '__main__':
    scaler = ShapeScaler(scale_factor=1.5)
    rectangle_area = scaler.scaled_area_rectangle(width=4, height=6)
    circle_area = scaler.scaled_area_circle(radius=3)
    print(rectangle_area)
    print(circle_area)