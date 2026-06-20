import math

class ShapeCalculator:
    def __init__(self, scale_factor):
        self.scale_factor = scale_factor

    def scaled_area_rectangle(self, width, height):
        scaled_width = width * self.scale_factor
        scaled_height = height * self.scale_factor
        return scaled_width * scaled_height

    def scaled_area_circle(self, radius):
        scaled_radius = radius * self.scale_factor
        return math.pi * (scaled_radius ** 2)

if __name__ == '__main__':
    scale = 2.5
    calc = ShapeCalculator(scale)
    rect_result = calc.scaled_area_rectangle(10, 5)
    circle_result = calc.scaled_area_circle(4)
    print(rect_result)
    print(circle_result)