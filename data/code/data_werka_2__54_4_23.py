import math

class Circle:
    PI = math.pi
    
    @staticmethod
    def calculate_radius(diameter):
        return diameter / 2
    
    @staticmethod
    def area_from_diameter(diameter):
        radius = Circle.calculate_radius(diameter)
        return Circle.PI * (radius ** 2)

if __name__ == '__main__':
    sample_diameters = [10, 25, 50]
    for diameter in sample_diameters:
        print(f"Area of a circle with diameter {diameter}: {Circle.area_from_diameter(diameter)}")