import math

class Circle:
    PI = math.pi
    
    @staticmethod
    def get_area(radius):
        return Circle.PI * radius ** 2

if __name__ == '__main__':
    sample_radius1 = 5.0
    area1 = Circle.get_area(sample_radius1)
    print(f"Area of circle with radius {sample_radius1}: {area1}")
    
    sample_radius2 = 10.5
    area2 = Circle.get_area(sample_radius2)
    print(f"Area of circle with radius {sample_radius2}: {area2}")