import math

class AreaCalculator:
    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2
    
    @staticmethod
    def square_area(side_length):
        return side_length ** 2

if __name__ == '__main__':
    circle_radius = 5
    square_side_length = 6
    
    circ_area = AreaCalculator.circle_area(circle_radius)
    sqr_area = AreaCalculator.square_area(square_side_length)
    
    print(f"Circle area: {circ_area}")
    print(f"Square area: {sqr_area}")
    
    if circ_area > sqr_area:
        print("The circle has a larger area.")