import math

class CircleCircumferenceCalculator:
    PI = 2 * math.pi
    
    @staticmethod
    def calculate_circumference(radius):
        return CircleCircumferenceCalculator.PI * radius

if __name__ == '__main__':
    sample_radius = 3.14
    calculator = CircleCircumferenceCalculator()
    circumference = calculator.calculate_circumference(sample_radius)
    print(circumference)