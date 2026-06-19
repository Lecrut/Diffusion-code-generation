import math

class CircleCalculator:
    PI = math.pi
    
    @staticmethod
    def calculate_area(radius):
        return CircleCalculator.PI * (radius ** 2)
    
    @staticmethod
    def calculate_areas(radii):
        areas = {}
        for radius in radii:
            areas[radius] = CircleCalculator.calculate_area(radius)
        return areas

if __name__ == '__main__':
    sample_radii = [3, 5.5, 7, 10]
    areas_dict = CircleCalculator.calculate_areas(sample_radii)
    print(areas_dict)