import math

class AreaComparer:
    @staticmethod
    def circle_area(radius):
        return math.pi * (radius ** 2)
    
    @staticmethod
    def square_area(side_length):
        return side_length ** 2
    
    @classmethod
    def compare_areas(cls, radius, side_length):
        circle = cls.circle_area(radius)
        square = cls.square_area(side_length)
        return circle == square

if __name__ == '__main__':
    r1 = 5.0
    l1 = 7.0
    print(f"Radius: {r1}, Length: {l1}, Areas Equal: {AreaComparer.compare_areas(r1, l1)}")
    
    r2 = 3.0
    l2 = math.pi * 3.0
    print(f"Radius: {r2}, Length: {l2}, Areas Equal: {AreaComparer.compare_areas(r2, l2)}")
    
    r3 = 1.0
    l3 = math.pi
    print(f"Radius: {r3}, Length: {l3}, Areas Equal: {AreaComparer.compare_areas(r3, l3)}")