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
    
    rectangle_width = 4
    rectangle_height = 6
    circle_radius = 3
    
    print(scaler.scaled_area_rectangle(rectangle_width, rectangle_height))
    print(scaler.scaled_area_circle(circle_radius))