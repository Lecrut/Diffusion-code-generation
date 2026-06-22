class AreaCalculator:
    def get_difference(self, area_a, area_b):
        return abs(area_a - area_b)

if __name__ == '__main__':
    calculator = AreaCalculator()
    
    area1 = 100.56
    area2 = 45.32
    difference1 = calculator.get_difference(area1, area2)
    print(f"The positive difference between {area1} and {area2} is: {difference1:.2f}")
    
    area3 = 78.90
    area4 = 78.90
    difference2 = calculator.get_difference(area3, area4)
    print(f"The positive difference between {area3} and {area4} is: {difference2:.2f}")
    
    area5 = 123.45
    area6 = 67.89
    difference3 = calculator.get_difference(area5, area6)
    print(f"The positive difference between {area5} and {area6} is: {difference3:.2f}")