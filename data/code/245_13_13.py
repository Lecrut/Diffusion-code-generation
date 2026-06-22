import math

class GeometryCalculator:
    def polygon_area(self, sides, circumradius):
        return (sides * (circumradius ** 2)) / (4 * math.tan(math.pi / sides))

    def circle_area(self, radius):
        return math.pi * (radius ** 2)

if __name__ == '__main__':
    calculator = GeometryCalculator()
    
    sample_sides = 6
    sample_circumradius = 5
    sample_radius = 3
    
    polygon_area_result = calculator.polygon_area(sample_sides, sample_circumradius)
    circle_area_result = calculator.circle_area(sample_radius)
    
    print(f"Polygon area: {polygon_area_result}")
    print(f"Circle area: {circle_area_result}")