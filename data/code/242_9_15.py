import math

class AreaCalculator:
    def semicircle_area(self, radius):
        return 0.5 * math.pi * radius ** 2
    
    def rectangle_area(self, width, height):
        return width * height

if __name__ == '__main__':
    calculator = AreaCalculator()
    semicircle_radius = 4
    rectangle_width = 6
    rectangle_height = 3
    semicircle_a = calculator.semicircle_area(semicircle_radius)
    rectangle_a = calculator.rectangle_area(rectangle_width, rectangle_height)
    print(f"Semicircle area: {semicircle_a:.10f}")
    print(f"Rectangle area: {rectangle_a:.10f}")