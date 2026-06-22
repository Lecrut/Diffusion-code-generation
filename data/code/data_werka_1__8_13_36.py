import math

class ShapeScaler:
    def __init__(self, scale_factor):
        self.scale_factor = scale_factor

    def scaled_area_rectangle(self, width, height):
        return (width * self.scale_factor) * (height * self.scale_factor)

    def scaled_area_circle(self, radius):
        return math.pi * (radius * self.scale_factor) ** 2

if __name__ == '__main__':
    scaler = ShapeScaler(2.5)
    rect_area = scaler.scaled_area_rectangle(4, 6)
    circle_area = scaler.scaled_area_circle(3)
    print(rect_area)
    print(circle_area)