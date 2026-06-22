import math

class Circle:
    PI = 2 * math.pi
    
    @staticmethod
    def calculate_radius(circumference):
        if circumference > 0:
            return circumference / Circle.PI
        else:
            return 0

if __name__ == '__main__':
    sample_circumference = 62.831853
    radius = Circle.calculate_radius(sample_circumference)
    print(f"Radius: {radius}")