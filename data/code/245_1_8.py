import math

class GeometryComparison:
    def __init__(self, radius, length):
        self.circle_area = math.pi * (radius ** 2)
        self.rectangle_area = length * length
    
    def check_equal_areas(self):
        return self.circle_area == self.rectangle_area

if __name__ == '__main__':
    g1 = GeometryComparison(5.0, 7.0)
    print(f"Radius: {g1.circle_area}, Length: {g1.rectangle_area}, Areas Equal: {g1.check_equal_areas()}")
    
    g2 = GeometryComparison(3.0, math.pi * 3.0)
    print(f"Radius: {g2.circle_area}, Length: {g2.rectangle_area}, Areas Equal: {g2.check_equal_areas()}")
    
    g3 = GeometryComparison(1.0, math.pi)
    print(f"Radius: {g3.circle_area}, Length: {g3.rectangle_area}, Areas Equal: {g3.check_equal_areas()}")