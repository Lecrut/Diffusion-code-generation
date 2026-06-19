import math

class CircleCalculator:
    PI = math.pi
    
    @staticmethod
    def calculate_area(radius):
        return CircleCalculator.PI * (radius ** 2)
    
    @staticmethod
    def calculate_areas_for_radii(radii_list):
        area_dict = {}
        for radius in radii_list:
            area_dict[radius] = CircleCalculator.calculate_area(radius)
        return area_dict

if __name__ == '__main__':
    sample_radii = [3.0, 7.5, 10.0]
    areas = CircleCalculator.calculate_areas_for_radii(sample_radii)
    print(areas)