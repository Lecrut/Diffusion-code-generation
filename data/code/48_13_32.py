import math

class Triangle:
    BASE = 6.0
    HEIGHT = 8.0
    
    @staticmethod
    def calculate_hypotenuse(base, height):
        return math.sqrt(base**2 + height**2)
    
    @staticmethod
    def calculate_area(base, height):
        return 0.5 * base * height

if __name__ == '__main__':
    hypotenuse = Triangle.calculate_hypotenuse(Triangle.BASE, Triangle.HEIGHT)
    area = Triangle.calculate_area(Triangle.BASE, Triangle.HEIGHT)
    print(f"Hypotenuse: {hypotenuse}")
    print(f"Area: {area}")