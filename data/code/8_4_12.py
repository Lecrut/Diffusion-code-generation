import math

class CircleAreaCalculator:
    def compute(self, radius):
        return math.pi * radius * radius

if __name__ == '__main__':
    calc = CircleAreaCalculator()
    print(calc.compute(3))
    print(calc.compute(7.5))
    print(calc.compute(100))