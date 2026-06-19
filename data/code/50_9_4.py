class AreaCalculator:

    def get_difference(self, area_a, area_b):
        return abs(area_a - area_b)
if __name__ == '__main__':
    calculator = AreaCalculator()
    area1 = 100.56
    area2 = 45.34
    area3 = 78.9
    difference1 = calculator.get_difference(area1, area2)
    difference2 = calculator.get_difference(area2, area3)
    print(f'Difference between {area1} and {area2}: {difference1:.2f}')
    print(f'Difference between {area2} and {area3}: {difference2:.2f}')