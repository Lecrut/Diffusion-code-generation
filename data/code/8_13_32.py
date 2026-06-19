import math

class ShapeScaler:
    def __init__(self, scale_factor):
        self.scale_factor = scale_factor

    def scaled_area_rectangle(self, width, height):
        area = width * height
        return area * self.scale_factor

    def scaled_area_circle(self, radius):
        area = math.pi * (radius ** 2)
        return area * self.scale_factor

if __name__ == '__main__':
    scaler = ShapeScaler(scale_factor=2.5)
    
    rectangle_width = 3
    rectangle_height = 4
    circle_radius = 5
    
    scaled_rectangle_area = scaler.scaled_area_rectangle(rectangle_width, rectangle_height)
    scaled_circle_area = scaler.scaled_area_circle(circle_radius)
    
    print(scaled_rectangle_area)
    print(scaled_circle_area)