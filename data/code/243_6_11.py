import math

class Circle:
    RADIUS = 100
    PERIMETER_FORMULA = lambda r: 2 * math.pi * r
    
    @staticmethod
    def calculate_perimeter():
        return Circle.PERIMETER_FORMULA(Circle.RADIUS)

if __name__ == '__main__':
    print(Circle.calculate_perimeter())