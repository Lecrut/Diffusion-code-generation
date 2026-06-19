import math

class ShapeScaler:
    def __init__(self, rectangles, circles, scale_factor):
        self.rectangles = rectangles
        self.circles = circles
        self.scale_factor = scale_factor

    def calculate_scaled_area(self):
        scaled_areas = []
        for rect in self.rectangles:
            width, height = rect
            original_area = width * height
            scaled_area = original_area * self.scale_factor ** 2
            scaled_areas.append(scaled_area)

        for circle in self.circles:
            radius = circle
            original_area = math.pi * (radius ** 2)
            scaled_area = original_area * self.scale_factor ** 2
            scaled_areas.append(scaled_area)

        return scaled_areas

if __name__ == '__main__':
    rectangles = [(3, 4), (5, 6)]
    circles = [2, 3]
    scale_factor = 1.5
    scaler = ShapeScaler(rectangles, circles, scale_factor)
    print(scaler.calculate_scaled_area())